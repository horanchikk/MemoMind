# -*- coding: utf-8 -*-
"""
Provides working with users.

User:
    uid [integer]
    first name [string]
    last name [string]
    login [string]
    email [string]
    password [string]
    access_token [string]
    notes [array of IDs]
    desks [array of IDs]
    notes_trash [array of IDs]
    desks_trash [array of IDs]
Note:
    nid [integer]
    author [integer]
    title [string]
    data [string]  # stores in markdown format
    cover [string]  # path to cover file
    gradient [array]  # aray of HEX colors
    created_at [integer]
    edited_at [integer]
Desk:
    did [integer]
    author [integer]
    title [string]
    columns [array of IDs]
DeskColumn:
    did [integer]
    title [string]
    cards [array of IDs]
DeskCard:
    did [integer]
    title [string]
    description [string]
    label [array od IDs]
    properties [array of IDs]
DeskCardLabel:
    did [integer]
    title [string]
    color [string]  # HEX string
DeskProperty:
    pid [integer]
    ptype [integer]  # ID of property type
    object [object]  # object data
PropertyType:
    pid [integer]
    title [string]
"""

from pymongo import MongoClient

db = MongoClient('localhost', 27017)
collection = db.get_database('MemoMind')
user = collection['user']
note = collection['note']
desk = collection['desk']
desk_column = collection['desk_column']
desk_card = collection['desk_card']
desk_card_label = collection['desk_card_label']
desk_property = collection['desk_property']
property_type = collection['property_type']
