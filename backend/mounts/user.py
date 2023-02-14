# -*- coding: utf-8 -*-
from secrets import token_hex

from fastapi import FastAPI, Request
from werkzeug.security import generate_password_hash, check_password_hash

from ..database import user
from ..exceptions import Error
from ..models import SignUpUser, LogInUser
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


@user_app.get('/id{uid}')
async def get_user_by_id(uid: int):
    """
    Finds user by ID
    """
    u = user.find_one({'uid': uid})
    if u is None:
        return Error.UserIsNotExists
    return {'response': u}
