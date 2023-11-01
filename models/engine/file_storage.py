#!/usr/bin/python3
import json
from models.base_model import BaseModel
"""
Contains a class File Storage
which serializes instances to a JSON file
and deserializes JSON file to instances
"""


class FileStorage:
    """Serializes instances to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        name = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[name] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            for key, obj in self.__objects.items():
                serialized_objects[key] = obj.to_dict()
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists)"""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.loads(f.read())
                for key, obj in self.__objects.items():
                    self.__objects[key] = eval(obj["__class__"])(**obj)
        except FileNotFoundError:
            pass
