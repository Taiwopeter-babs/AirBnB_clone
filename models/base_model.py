#!/usr/bin/python3
"""
    This module defines a class `BaseModel` that
    every other class inherits from
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    Base class for all other classes

    """

    def __init__(self, *args, **kwargs):
        """
            class constructor: creates a new instance from kwargs
            if it is not empty
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Prints a string representation of instance"""
        cls_name = type(self).__name__
        uid = self.id
        dict_rep = self.__dict__

        return "[{}] ({}) {}".format(cls_name, uid, dict_rep)

    def save(self):
        """Updates the updated_at attribute with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary instance of __dict__"""
        new_dict = self.__dict__.copy()

        string_created = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        string_updated = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = string_created
        new_dict["updated_at"] = string_updated

        return (new_dict)
