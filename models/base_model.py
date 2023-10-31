#!/usr/bin/python3
"""Module BaseModel Class """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """init method"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()        

        def save(self):
            """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def __str__(self):
        """Returns a string representation of the instance"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
