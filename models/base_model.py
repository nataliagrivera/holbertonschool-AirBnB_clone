#!/usr/bin/python3
"""Module BaseModel Class"""
# Import necessary modules
from datetime import datetime
from uuid import uuid4
import json


# Define the BaseModel class
class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialization method
        Args:
            *args: unsused argument.
            **kwargs: pairs of key/value (dictionary)

        Attributes:
            id: unique id given by uuid4()
            create_at: datetime when the object is created
            updated_at: datetime when the object is updated"""
        for k, v in kwargs.items():
            if k in ['created_at', 'updated_at']:
                setattr(self, k, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
            else:
                setattr(self, k, v)

        else:
            # If no keyword arguments are provided, generate new values
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            
    def __str__(self):
        """str method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at with datetime"""
        self.updated_at = datetime.now()  # Update the update date and time

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ """
        new_dict = self.__dict__.copy()  # Create a copy of the instances
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
