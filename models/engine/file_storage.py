#!/usr/bin/python3
import json
import os
import models
"""
Contains a class File Storage
which serializes instances to a JSON file
and deserializes JSON file to instances
"""

class FileStorage:
    _file_path = "file.json"
    _objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage._objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        name = f"{obj.__class__.__name__}.{obj.id}"
        self._objects[name] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in self._objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self._file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)"""
        if os.path.isfile(self._file_path):
            with open(self._file_path, 'r') as f:
                self._objects = json.loads(f.read())
                for key, obj_dict in self._objects.items():
                    self._objects[key] = eval(obj_dict["__class__"])(**obj_dict)

        else:
            pass
