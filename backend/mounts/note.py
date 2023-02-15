# -*- coding: utf-8 -*-
from time import time

import pymongo
from fastapi import FastAPI, Request

from ..exceptions import Error
from ..utils import get_body
from ..database import note, user
from ..models import EditNote, CreateNote, NoteModel

note_app = FastAPI()


@note_app.middleware('http')
async def check_request(req: Request, call_next):
    if req.method in ['PUT', 'PATCH', 'POST']:
        body = get_body(req)
        if 'access_token' in req.query_params:
            u = user.find_one({'access_token': req.query_params['access_token']})
            if u is None:
                return Error.AccessDenied
        else:
            return Error.AccessDenied
    return await call_next(req)


@note_app.post('/')
async def create_new_note(data: CreateNote, access_token: str):
    """
    Creates a new note
    """
    u = user.find_one({'access_token': access_token})
    nid = note.estimated_document_count()
    if nid != 0:
        n = note.find_one({}, sort=[('_id', pymongo.DESCENDING)])
        nid = n['nid'] + 1
    new_note = {
        'nid': nid,
        'title': data.title,
        'author': u['uid'],
        'data': '',
        'cover': '',
        'gradient': ['#8A2387', '#E94057', '#F27121'],
        'public': '',
        'created_at': time(),
        'edited_at': -1,
    }
    user.update_one({'uid': u['uid']}, {'$push': {'notes': nid}})
    note.insert_one(new_note)
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
    if not n['public'] and n['author'] != u['uid']:
        return Error.AccessDenied
    return {'response': NoteModel(**n)}


@note_app.patch('/id{nid}')
async def edit_note(data: EditNote, nid: int, access_token: str):
    """
    Edits note
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.UserIsNotExists
    n = note.find_one({'nid': nid})
    if n is None:
        return Error.NoteIsNotExists
    if n['author'] != u['uid']:
        return Error.AccessDenied
    n = NoteModel(**n)
    note.update_one({'nid': nid}, {'$set': {
        'title': data.title if data.title else n.title,
        'data': data.data,
        'gradient': data.gradient,
        'cover': data.cover,
        'edited_at': time()
    }})
    return {'response': 'success'}


@note_app.patch('/share')
async def share_note(note_id: int, access_token: str, note_name: str):
    """
    Shares the note for public view. length of `note_name` should be larger than 6 symbols
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    n = note.find_one({'nid': note_id})
    if n is None:
        return Error.NoteIsNotExists
    if n['author'] != u['uid']:
        return Error.AccessDenied
    n = note.find_one({'public': note_name})
    if n is not None:
        return Error.NoteNameIsExits
    if note_name.startswith('id'):
        return Error.NoteCantStartsWithId
    note.update_one({'nid': note_id}, {'$set': {'public': note_name}})
    return {'response': 'success'}


@note_app.patch('/unshare')
async def unshare_note(note_id: int, access_token: str):
    """
    Unshares note by `note_id`

    :param note_id: note ID
    :param access_token: user token
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    n = note.find_one({'nid': note_id})
    if n is None:
        return Error.NoteIsNotExists
    if n['author'] != u['uid']:
        return Error.AccessDenied
    note.update_one({'nid': note_id}, {'$set': {'public': ''}})
    return {'response': 'success'}


@note_app.patch('/favorite')
async def add_note_to_favorite(note_id: int, access_token: str):
    """
    Toggles note favorite

    :param note_id: note ID
    :param access_token: user token
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    n = note.find_one({'nid': note_id})
    if n is None:
        return Error.NoteIsNotExists
    if n['author'] != u['uid']:
        return Error.AccessDenied
    if note_id in u['notes_favorite']:
        note.update_one({'nid': note_id}, {'$pull': {'notes_favorite': {'$eq': note_id}}})
        return {'response': False}
    note.update_one({'nid': note_id}, {'$push': {'notes_favorite': note_id}})
    return {'response': True}


@note_app.delete('/id{note_id}')
async def add_note_to_favorite(note_id: int, access_token: str):
    """
    Moves note into trash or delete it.

    :param note_id: note ID
    :param access_token: user token
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    n = note.find_one({'nid': note_id})
    if n is None:
        return Error.NoteIsNotExists
    if n['author'] != u['uid']:
        return Error.AccessDenied
    if note_id not in u['notes'] and note_id not in u['notes_trash']:
        return Error.NoteIsNotExists
    if note_id in u['notes']:
        user.update_one(
            {'uid': u['uid']}, {'$push': {'notes_trash': note_id}}
        )
        user.update_one(
            {'uid': u['uid']}, {'$pull': {'notes': note_id}}
        )
    else:
        user.update_one(
            {'uid': u['uid']}, {'$pull': {'notes_trash': note_id}}
        )
        note.delete_one({'nid': note_id})
    return {'response': 'success'}


@note_app.patch('/restore{note_id}')
async def add_note_to_favorite(note_id: int, access_token: str):
    """
    Restores note from trash

    :param note_id: note ID
    :param access_token: user token
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    n = note.find_one({'nid': note_id})
    if n is None:
        return Error.NoteIsNotExists
    if n['author'] != u['uid']:
        return Error.AccessDenied
    if note_id not in u['notes_trash']:
        return Error.NoteIsNotExists
    user.update_one(
        {'uid': u['uid']}, {'$pull': {'notes_trash': note_id}}
    )
    user.update_one(
        {'uid': u['uid']}, {'$push': {'notes': note_id}}
    )
    return {'response': 'success'}


@note_app.get('/{note_name}')
async def get_note_by_id(note_name: str):
    """
    Finds note by its ID
    """
    n = note.find_one({'public': note_name})
    if n is None:
        return Error.NoteIsNotExists
    return {'response': NoteModel(**n)}