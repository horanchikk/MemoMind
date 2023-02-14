# -*- coding: utf-8 -*-
from pydantic import BaseModel


class SignUpUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    login: str
    password: str


class LogInUser(BaseModel):
    login: str
    password: str


class CreateNote(BaseModel):
    title: str


class EditNote(BaseModel):
    id: int
    title: str
    data: str
    cover: str
    gradient: list[str]
    use_cover: bool
