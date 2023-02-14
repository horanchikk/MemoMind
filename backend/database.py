# -*- coding: utf-8 -*-
"""
Provides working with users.

User:
    id [integer]
    first name [string]
    last name [string]
    email [string]
    password [string]
    notes [array of IDs]
    desks [array of IDs]
Note:
    id [integer]
    title [string]
    data [string]  # stores in markdown format
    cover [string]  # path to cover file
    gradient [array]  # aray of HEX colors
    use_cover [bool]
Desk:
    id [integer]
    title [string]
    columns [array of IDs]
DeskColumn:
    id [integer]
    title [string]
    cards [array of IDs]
DeskCard:
    id [integer]
    title [string]
    description [string]
    label [array od IDs]
    properties [array of IDs]
DeskCardLabel:
    id [integer]
    title [string]
    color [string]  # HEX string
DeskProperty:
    id [integer]
    ptype [integer]  # ID of property type
    object [object]  # object data
PropertyType:
    id [integer]
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
