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
Note:
    id [integer]
    title [string]
    data [string]  # stores in markdown format
    cover [string]  # path to cover file
    gradient [array]  # aray of HEX colors
    use_cover [bool]
"""

from pymongo import MongoClient

db = MongoClient('localhost', 27017)
collection = db.get_database('MemoMind')
uc = collection['user']
