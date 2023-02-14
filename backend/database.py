# -*- coding: utf-8 -*-
"""
Provides working with users.
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
