#!/usr/bin/python3
"""Initialize the models package"""

import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Determine the type of storage to use based on environment variable
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()

