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
