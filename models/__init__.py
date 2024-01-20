#!/usr/bin/python3
"""Initialize the models package"""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

storage_t = getenv('HBNB_TYPE_STORAGE')

# Determine the type of storage to use based on environment variable
if storage_t == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
