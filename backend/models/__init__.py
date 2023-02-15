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


class CreateDesk(BaseModel):
    title: str


class EditDesk(BaseModel):
    title: str


class EditLabel(BaseModel):
    title: str
    color: str


class EditColumn(BaseModel):
    title: str


class CreateLabel(BaseModel):
    did: int
    title: str
    color: str


class EditCard(BaseModel):
    title: str
    description: str
    labels: list[int]
    properties: list[dict[str, object]]


class CreateColumn(BaseModel):
    did: int
    title: str


class CreateColumnCard(BaseModel):
    did: int
    cid: int
    title: str
    description: str
    labels: list[int]
    properties: list[dict[str, object]]


class UserModel(BaseModel):
    first_name: str
    last_name: str
    login: str
    email: str
    password: str
    access_token: str
    notes: list[int]
    desks: list[int]
    notes_favorite: list[int]
    desks_favorite: list[int]
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


class DeskCardLabelModel(BaseModel):
    title: str
    color: str  # HEX string


class DeskCardModel(BaseModel):
    title: str
    description: str
    labels: list[int] = []  # list of indexes
    properties: list[dict[str, object]] = []


class DeskColumnModel(BaseModel):
    cid: int
    title: str
    cards: list[DeskCardModel]


class DeskModel(BaseModel):
    did: int
    author: int
    title: str
    public: str
    created_at: int
    edited_at: int
    labels: list[DeskCardLabelModel]
    columns: list[DeskColumnModel]
