# -*- coding:utf-8 -*-
from time import time

import pymongo
from fastapi import FastAPI, Request

from ..exceptions import Error
from ..models import (
    DeskModel, DeskCardModel, DeskCardLabelModel,
    DeskColumnModel, CreateDesk, CreateLabel,
    CreateColumn, CreateColumnCard, EditDesk, EditLabel, EditColumn, EditCard
)
from ..database import (
    user, desk
)
from ..utils import get_body


desk_app = FastAPI()


@desk_app.middleware('http')
async def check_request(req: Request, call_next):
    if req.method in ['PUT', 'PATCH', 'POST']:
        body = await get_body(req)
        if 'access_token' in req.query_params:
            u = user.find_one({'access_token': req.query_params['access_token']})
            if u is None:
                return Error.AccessDenied
        else:
            return Error.AccessDenied
    return await call_next(req)


@desk_app.post('/')
async def create_new(data: CreateDesk, access_token: str):
    """
    Creates a new desk for user
    """
    u = user.find_one({'access_token': access_token})
    did = desk.estimated_document_count()
    if did != 0:
        d = desk.find_one({}, sort=[('_id', pymongo.DESCENDING)])
        did = d['did'] + 1
    desk_data = {
        'did': did,
        'title': data.title,
        'author': u['uid'],
        'columns': [],
        'public': '',
        'created_at': time(),
        'edited_at': -1,
        'labels': [
            {'title': 'Срочно', 'color': '#F04D64'},
            {'title': 'Запланировано', 'color': '#654A87'},
            {'title': 'Документы', 'color': '#6E96E0'},
            {'title': 'Перенесено', 'color': '#F99836'},
            {'title': 'В процессе', 'color': '#FFDA3D'},
            {'title': 'Готово', 'color': '#D0FF6C'},
        ]
    }
    desk.insert_one(desk_data)
    user.update_one({'uid': u['uid']}, {'$push': {'desks': did}})
    return {'response': {
        'did': did
    }}


@desk_app.post('/label')
async def create_new_label(data: CreateLabel, access_token: str):
    """
    Creates a new label
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.UserIsNotExists
    d = desk.find_one({'did': data.did})
    if d is None:
        return Error.DeskIsNotExists
    if d['author'] != u['uid']:
        return Error.AccessDenied
    data_label = DeskCardLabelModel(title=data.title, color=data.color)
    desk.update_one({'did': data.did}, {'$push': {'labels': data_label.dict()}})
    return {'response': {
        'label_index': len(d['labels'])
    }}


@desk_app.post('/column')
async def create_new_column(data: CreateColumn, access_token: str):
    """
    Creates a new column for desk
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    d = desk.find_one({'did': data.did})
    if d is None:
        return Error.DeskIsNotExists
    if d['author'] != u['uid']:
        return Error.AccessDenied
    column = DeskColumnModel(title=data.title, cards=[], cid=len(d['columns']))
    desk.update_one({'did': data.did}, {'$push': {'columns': column.dict()}})
    return {'response': {
        'column_index': len(d['columns'])
    }}


@desk_app.post('/column-card')
async def create_column_card(data: CreateColumnCard, access_token: str):
    """
    Creates a new column card
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    d = desk.find_one({'did': data.did})
    if d is None:
        return Error.DeskIsNotExists
    if d['author'] != u['uid']:
        return Error.AccessDenied
    card = DeskCardModel(
        title=data.title,
        description=data.description,
        labels=data.labels,
        properties=data.properties
    )
    desk.update_one(
        {'did': data.did, 'columns.cid': data.cid},
        {'$push': {'columns.$.cards': card.dict()}}
    )
    return {'response': {
        'card_index': len(d['columns'][data.cid]['cards'])
    }}


@desk_app.get('/id{did}/label{label_index}')
async def get_label_by_label_index(did: int, label_index: int, access_token: str):
    """
    Finds label by desk ID and label_index
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    d = desk.find_one({'did': did})
    if d is None:
        return Error.DeskIsNotExists
    if d['author'] != u['uid']:
        return Error.AccessDenied
    if label_index >= len(d['labels']) or label_index < 0:
        return Error.IndexError
    return {'response': d['labels'][label_index]}


@desk_app.get('/id{did}/column{column_index}')
async def get_column_by_column_index(did: int, column_index: int, access_token: str):
    """
    Finds column by desk ID and label_index
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    d = desk.find_one({'did': did})
    if d is None:
        return Error.DeskIsNotExists
    if d['author'] != u['uid']:
        return Error.AccessDenied
    if column_index >= len(d['columns']) or column_index < 0:
        return Error.IndexError
    return {'response': d['columns'][column_index]}


@desk_app.get('/id{did}')
async def get_desk_by_id(did: int, access_token: str):
    """
    Finds desk by ID
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    d = desk.find_one({'did': did})
    if d is None:
        return Error.DeskIsNotExists
    return {'response': DeskModel(**d)}


@desk_app.patch('/id{did}/label{label_index}')
async def edit_label(data: EditLabel, did: int, label_index: int, access_token: str):
    """
    Moves column in desk
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    d = desk.find_one({'did': did})
    if d is None:
        return Error.DeskIsNotExists
    if d['author'] != u['uid']:
        return Error.AccessDenied
    if label_index < 0 or label_index >= len(d['labels']):
        return Error.IndexError
    desk.update_one(
        {'did': did},
        {'$set': {
            f'labels.{label_index}': {
                'title': data.title,
                'color': data.color
            }
        }}
    )
    return {'response': 'success'}


@desk_app.patch('/id{did}/column{cid}/card{card_index}/move')
async def move_card(
        did: int,
        cid: int,
        card_index: int,
        new_cid: int,
        new_card_index: int,
        access_token: str
):
    """
    Moves card in desk

    :param did: desk ID
    :param cid: Column ID
    :param card_index: Card index in column
    :param new_card_index: New card index in column
    :param new_cid: new column ID
    :param access_token: user access_token
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    d = desk.find_one({'did': did})
    if d is None:
        return Error.DeskIsNotExists
    if d['author'] != u['uid']:
        return Error.AccessDenied
    if cid < 0 or cid >= len(d['columns']):
        return Error.IndexError
    if new_cid < 0 or new_cid >= len(d['columns']):
        return Error.IndexError
    c = list(filter(lambda x: x['cid'] == cid, d['columns']))[0]
    new_c = list(filter(lambda x: x['cid'] == new_cid, d['columns']))[0]
    if card_index < 0 or card_index >= len(c['cards']):
        return Error.IndexError
    if new_card_index < 0 or new_card_index > len(new_c['cards']):
        return Error.IndexError
    card = c['cards'][card_index]
    desk.update_one(
        {'did': did, 'columns.cid': cid},
        {'$unset': {f'columns.$.cards.{card_index}': 1}}
    )
    desk.update_one(
        {'did': did, 'columns.cid': cid},
        {'$pull': {f'columns.$.cards': {'$eq': None}}}
    )
    desk.update_one(
        {'did': did, 'columns.cid': new_cid},
        {'$push': {'columns.$.cards': {
            '$each': [card],
            '$position': new_card_index
        }}}
    )
    d = desk.find_one({'did': did})
    return {'response': 'success'}


@desk_app.patch('/id{did}/column{cid}/card{card_index}')
async def edit_card(
        data: EditCard,
        did: int,
        cid: int,
        card_index: int,
        access_token: str
):
    """
    Edits card in desk

    :param data: edit card data
    :param did: desk ID
    :param cid: Column ID
    :param card_index: Card index in column
    :param access_token: user access_token
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    d = desk.find_one({'did': did})
    if d is None:
        return Error.DeskIsNotExists
    if d['author'] != u['uid']:
        return Error.AccessDenied
    if cid < 0 or cid >= len(d['columns']):
        return Error.IndexError
    c = list(filter(lambda x: x['cid'] == cid, d['columns']))[0]
    if card_index < 0 or card_index >= len(c['cards']):
        return Error.IndexError
    if not data.title:
        return Error.TitleIsEmpty
    desk.update_one(
        {'did': did, 'columns.cid': cid},
        {'$set': {
            f'columns.$.cards.{card_index}.title': data.title,
            f'columns.$.cards.{card_index}.description': data.description,
            f'columns.$.cards.{card_index}.labels': data.labels,
            f'columns.$.cards.{card_index}.properties': data.properties,
        }},
    )
    return {'response': 'success'}


@desk_app.patch('/id{did}/column{cid}/move')
async def move_column(did: int, cid: int, new_cid: int, access_token: str):
    """
    Moves column in desk
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    d = desk.find_one({'did': did})
    if d is None:
        return Error.DeskIsNotExists
    if d['author'] != u['uid']:
        return Error.AccessDenied
    if cid < 0 or cid >= len(d['columns']):
        return Error.IndexError
    if new_cid < 0 or new_cid >= len(d['columns']):
        return Error.IndexError
    c = list(filter(lambda x: x['cid'] == cid, d['columns']))[0]
    desk.update_one(
        {'did': did},
        {'$pull': {'columns': {'cid': {'$eq': cid}}}}
    )
    desk.update_one(
        {'did': did},
        {'$push': {'columns': {
            '$each': [c],
            '$position': new_cid
        }}}
    )
    d = desk.find_one({'did': did})
    return {'response': 'success'}


@desk_app.patch('/id{did}/column{cid}')
async def edit_column(data: EditColumn, did: int, cid: int, access_token: str):
    """
    Edits column in desk
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    d = desk.find_one({'did': did})
    if d is None:
        return Error.DeskIsNotExists
    if d['author'] != u['uid']:
        return Error.AccessDenied
    if cid < 0 or cid >= len(d['columns']):
        return Error.IndexError
    if not data.title:
        return Error.TitleIsEmpty
    desk.update_one(
        {'did': did, 'columns.cid': cid},
        {'$set': {'columns.$.title': data.title}}
    )
    return {'response': 'success'}


@desk_app.patch('/id{did}')
async def edit_desk_by_id(data: EditDesk, did: int, access_token: str):
    """
    Edits desk by ID
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    d = desk.find_one({'did': did})
    if d is None:
        return Error.DeskIsNotExists
    if d['author'] != u['uid']:
        return Error.AccessDenied
    if not data.title:
        return Error.TitleIsEmpty
    desk.update_one({'did': did}, {'$set': data.dict()})
    return {'response': 'success'}


@desk_app.patch('/share')
async def share_note(desk_id: int, access_token: str, desk_name: str):
    """
    Shares the desk for public view. length of `desk_name` should be larger than 6 symbols
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    n = desk.find_one({'did': desk_id})
    if n is None:
        return Error.DeskIsNotExists
    if n['author'] != u['uid']:
        return Error.AccessDenied
    n = desk.find_one({'public': desk_name})
    if n is not None:
        return Error.DeskNameIsExits
    if desk_name.startswith('id'):
        return Error.DeskCantStartsWithId
    desk.update_one({'did': desk_id}, {'$set': {'public': desk_name}})
    return {'response': 'success'}


@desk_app.patch('/unshare')
async def unshare_note(desk_id: int, access_token: str):
    """
    Unshares desk by `note_id`

    :param desk_id: note ID
    :param access_token: user token
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    n = desk.find_one({'did': desk_id})
    if n is None:
        return Error.DeskIsNotExists
    if n['author'] != u['uid']:
        return Error.AccessDenied
    desk.update_one({'did': desk_id}, {'$set': {'public': ''}})
    return {'response': 'success'}


@desk_app.patch('/favorite')
async def add_desk_to_fav(desk_id: int, access_token: str):
    """
    Toggles note favorite

    :param desk_id: note ID
    :param access_token: user token
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    n = desk.find_one({'did': desk_id})
    if n is None:
        return Error.DeskIsNotExists
    if n['author'] != u['uid']:
        return Error.AccessDenied
    if desk_id in u['desks_favorite']:
        desk.update_one({'nid': desk_id}, {'$pull': {'desks_favorite': {'$eq': desk_id}}})
        return {'response': False}
    desk.update_one({'nid': desk_id}, {'$push': {'desks_favorite': desk_id}})
    return {'response': True}


@desk_app.delete('/id{desk_id}')
async def delete_desk(desk_id: int, access_token: str):
    """
    Moves desk into trash or delete it.

    :param desk_id: note ID
    :param access_token: user token
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    n = desk.find_one({'nid': desk_id})
    if n is None:
        return Error.DeskIsNotExists
    if n['author'] != u['uid']:
        return Error.AccessDenied
    if desk_id not in u['desks'] and desk_id not in u['desks_trash']:
        return Error.DeskIsNotExists
    if desk_id in u['desks']:
        user.update_one(
            {'uid': u['uid']}, {'$push': {'desks_trash': desk_id}}
        )
        user.update_one(
            {'uid': u['uid']}, {'$pull': {'desks': desk_id}}
        )
    else:
        user.update_one(
            {'uid': u['uid']}, {'$pull': {'desks_trash': desk_id}}
        )
        desk.delete_one({'did': desk_id})
    return {'response': 'success'}


@desk_app.patch('/restore{desk_id}')
async def restore_desk_from_trash(desk_id: int, access_token: str):
    """
    Restores desk from trash

    :param desk_id: note ID
    :param access_token: user token
    """
    u = user.find_one({'access_token': access_token})
    if u is None:
        return Error.AccessDenied
    n = desk.find_one({'did': desk_id})
    if n is None:
        return Error.NoteIsNotExists
    if n['author'] != u['uid']:
        return Error.AccessDenied
    if desk_id not in u['desks_trash']:
        return Error.NoteIsNotExists
    user.update_one(
        {'uid': u['uid']}, {'$pull': {'desks_trash': desk_id}}
    )
    user.update_one(
        {'uid': u['uid']}, {'$push': {'desks': desk_id}}
    )
    return {'response': 'success'}


@desk_app.get('/{desk_name}')
async def get_public_desk(desk_name: str):
    """
    Finds desk by its ID
    """
    n = desk.find_one({'public': desk_name})
    if n is None:
        return Error.NoteIsNotExists
    return {'response': DeskModel(**n)}
