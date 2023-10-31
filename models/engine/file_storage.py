#!/usr/bin/python3
"""File Storage"""
import json
import os.path


class FileStorage:
    def __init__(self):
        self._file_path = "file.json"
        self._objects = {}

    def all(self):
        return self._objects
    
    def new(self, obj):
        self._objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        with open(self._file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self._objects.items()}, f)

    def reload(self):
        if os.path.isfile(self._file_path):
            with open(self._file_path, 'r') as f:
                self._objects = {k: self._classes()[v['__class__']](**v) for k, v in json.load(f).items()}
