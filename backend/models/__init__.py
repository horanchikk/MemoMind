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


class EditUserProfile(BaseModel):
    old_password: str
    new_password: str


class CreateNote(BaseModel):
    title: str


class EditNote(BaseModel):
    title: str = ''
    data: str
    cover: str
    gradient: list[str] = []
    use_cover: bool


class UserModel(BaseModel):
    first_name: str
    last_name: str
    login: str
    email: str
    password: str
    access_token: str
    notes: list[int]
    desks: list[int]
    notes_trash: list[int]
    desks_trash: list[int]


class NoteModel(BaseModel):
    nid: int
    author: int
    title: str
    data: str  # stores in markdown format
    cover: str  # path to cover file
    gradient: list[str]  # aray of HEX colors
    created_at: int
    edited_at: int


class DeskModel(BaseModel):
    did: int
    author: int
    title: str
    columns: list[int]


class DeskColumnModel(BaseModel):
    did: int
    title: str
    cards: list[int]


class DeskCardModel(BaseModel):
    did: int
    title: str
    description: str
    label: list[int]
    properties: list[int]


class DeskCardLabelModel(BaseModel):
    did: int
    title: str
    color: str  # HEX string


class DeskPropertyModel(BaseModel):
    pid: int
    ptype: int  # ID of property type
    obj: dict[str, object]  # object data


class PropertyTypeModel(BaseModel):
    pid: int
    title: str
