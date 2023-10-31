#!/usr/bin/python3
"""Module BaseModel Class"""
# Import necessary modules
from datetime import datetime
from uuid import uuid4

# Define the BaseModel class
class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Initialization method"""
        if kwargs:
            # If keyword arguments are provided, initialize the instance attributes
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    # If the key is 'created_at' or 'updated_at', convert the value to a datetime object
                    setattr(self, k, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    # For other keys, set the attribute to the provided value
                    setattr(self, k, v)
        else:
            # If no keyword arguments are provided, generate new values for id, created_at, and updated_at
            self.id = str(uuid4())  # Generate a unique ID and convert it to a string
            self.created_at = datetime.now()  # Set the creation date and time to the current datetime
            self.updated_at = datetime.now()  # Set the update date and time to the current datetime

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()  # Update the update date and time to the current datetime

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()  # Create a copy of the instance's attribute dictionary
        new_dict["__class__"] = self.__class__.__name__  # Add a special key for the class name
        new_dict["created_at"] = self.created_at.isoformat()  # Convert the creation date and time to ISO format
        new_dict["updated_at"] = self.updated_at.isoformat()  # Convert the update date and time to ISO format
        return new_dict  # Return the resulting dictionary

    def __str__(self):
        """Returns a string representation of the instance"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
        # Return a string with the class name, ID, and the dictionary of instance attributes
