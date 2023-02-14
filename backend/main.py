# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .mounts import user_app, note_app


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_headers=['*'],
    allow_origins=['*'],
    allow_methods=['*'],
    allow_credentials=True
)

app.mount('/user', user_app)
app.mount('/note', note_app)
