# -*- coding: utf-8 -*-
from time import time

from fastapi import FastAPI, Request

from ..exceptions import Error
from ..utils import get_body
from ..database import note, user
from ..models import EditNote, CreateNote

note_app = FastAPI()


@note_app.middleware('http')
async def check_request(req: Request, call_next):
    if req.method in ['PUT', 'PATCH', 'POST']:
        body = get_body(req)
        if 'access_token' in req.query_params:
            u = user.find_one({'access_token': req.query_params['access_token']})
            if u is None:
                return Error.AccessDenied
        return Error.AccessDenied
    return await call_next(req)


@note_app.post('/')
async def create_new_note(data: CreateNote, access_token: str):
    """
    Creates a new note
    """
    u = user.find_one({'access_token': access_token})
    nid = note.estimated_document_count()
    new_note = {
        'nid': nid,
        'title': data.title,
        'author': u['uid'],
        'data': '',
        'cover': '',
        'gradient': [''],
        'created_at': time(),
        'edited_at': -1,
    }
    user.update_one({'uid': u.uid}, {'$push': {'notes': new_note}})
    return {'response': {
        'id': nid
    }}


@note_app.get('/id{nid}')
async def get_note_by_id(nid: int, access_token: str = ''):
    """
    Finds note by its ID
    """
    if not access_token:
        return Error.AccessDenied
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    n = note.find_one({'nid': nid})
    if n is None:
        return Error.NoteIsNotExists
    if n['author'] != u['uid']:
        return Error.AccessDenied
    return {'response': n}
