# -*- coding: utf-8 -*-
from secrets import token_hex

import pymongo
from fastapi import FastAPI, Request
from werkzeug.security import generate_password_hash, check_password_hash

from ..database import user
from ..exceptions import Error
from ..models import SignUpUser, LogInUser, EditUserProfile, UserModel
from ..utils import get_body

user_app = FastAPI()


@user_app.middleware('http')
async def check_request(req: Request, call_next):
    if req.method in ['PUT', 'PATCH']:
        body = get_body(req)
        if 'access_token' in req.query_params:
            u = user.find_one({'access_token': req.query_params['access_token']})
            if u is None:
                return Error.AccessDenied
        else:
            return Error.AccessDenied
    return await call_next(req)


@user_app.post('/register')
async def create_new_user(data: SignUpUser):
    """
    Creates a new user. E-mail and login should be unique
    """
    # Check if email is exists
    if user.find_one({'email': data.email}) is not None:
        return Error.EmailWasUsed
    # Check if login is exists
    if user.find_one({'login': data.email}) is not None:
        return Error.LoginWasUsed
    # Create user
    uid = user.estimated_document_count()
    if uid != 0:
        u = user.find_one({}, sort=[('_id', pymongo.DESCENDING)])
        uid = u['uid'] + 1
    token = token_hex(32)
    user.insert_one({
        'uid': uid,
        'password': generate_password_hash(data.password),
        'access_token': token,
        'login': data.login,
        'first_name': data.first_name,
        'last_name': data.last_name,
        'email': data.email,
        'notes': [],
        'desks': [],
        'font': '',
        'compact': False,
        'small_text': False,
        'notes_favorite': [],
        'desks_favorite': [],
        'notes_trash': [],
        'desks_trash': [],
    })
    return {'response': {
        'id': uid,
        'access_token': token
    }}


@user_app.post('/login')
async def log_in_user(data: LogInUser):
    """
    Logs in user account.
    """
    u = user.find_one({'login': data.login})
    if u is None:
        return Error.UserIsNotExists
    if not check_password_hash(data.password, u['password']):
        return Error.LoginOrPasswordIsNotCorrect
    return {'response': {
        'access_token': u['access_token']
    }}


@user_app.patch('/edit')
async def edit_user_profile(data: EditUserProfile, access_token: str):
    """
    Edits user profile
    """
    u = user.find_one({'access_token': access_token})
    if check_password_hash(data.old_password, u['password']):
        return Error.PasswordIsNotCorrect
    token = token_hex(32)
    user.update_one(
        {'access_token': access_token},
        {'$set': {
            'password': generate_password_hash(data.new_password),
            'access_token': token
        }}
    )
    return {'response': {'access_token': token}}


@user_app.patch('/font')
async def change_font(font: str, access_token: str):
    """
    Changes font in all notes and desks
    """
    if font not in ['default', 'serif', 'mono']:
        return Error.CanNotSetThisFont
    user.update_one({'access_token': access_token}, {'$set': {'font': font}})
    return {'response': 'success'}


@user_app.patch('/compact')
async def change_font(value: bool, access_token: str):
    """
    Toggles compact view
    """
    user.update_one({'access_token': access_token}, {'$set': {'compact': value}})
    return {'response': 'success'}


@user_app.patch('/small_text')
async def change_font(value: bool, access_token: str):
    """
    Toggles text size
    """
    user.update_one({'access_token': access_token}, {'$set': {'small_text': value}})
    return {'response': 'success'}


@user_app.get('/id{uid}')
async def get_user_by_id(uid: int):
    """
    Finds user by ID
    """
    u = user.find_one({'uid': uid})
    if u is None:
        return Error.UserIsNotExists
    u = UserModel(**u).dict()
    del u['access_token']
    del u['password']
    return {'response': u}
