#!/usr/bin/python3
"""File Storage"""
import json
import os.path
import os


class FileStorage:
    _file_path = "file.json"
    _objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage._objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        name = obj.__class__.__name__ + '.' + obj.id
        self._objects[name] = obj
        
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
            with open(self._file_path, 'w') as f:
                json.dump({k: v.to_dict() for k, v in self._objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""
        if os.path.isfile(self._file_path):
            with open(self._file_path, 'r') as f:
                self._objects = {k: self._classes()[v['__class__']](**v) for k, v in json.load(f).items()}
