#!/usr/bin/python3
"""
executes when model is imported
"""


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
