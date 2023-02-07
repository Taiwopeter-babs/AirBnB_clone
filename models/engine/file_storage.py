#!/usr/bin/python3
"""
    This module contains a class `FileStorage` that
    Serializes instances to JSON file & Deserializes JSON file
    to instances
"""
from models.base_model import BaseModel
import json
import models


class FileStorage:
    """
        Storage class that contains serialization and deserialization
        of objects and data structures & JSON files respectively

        Args:
            file_path(str): Path to JSON file. Private class attribute
            objects(dict): Storage of objects by their ids
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects obj variable with obj's id as key"""
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to json file"""
        old_dict = FileStorage.__objects

        new_dict = {obj: old_dict[obj].to_dict() for obj in old_dict.keys()}

        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            json.dump(new_dict, json_file)

    def reload(self):
        """Deserializes a JSON file to __objects instance"""
        file_path = FileStorage.__file_path

        try:
            with open(file_path, encoding="utf-8") as json_file:
                json_string = json_file.read()
            obj_dict = json.loads(json_string)
            """
                delete the __class__ attribute with respect to requirements
                of constructor in BaseModel.
            """
            for obj_val in obj_dict.values():
                cls_name = obj_val["__class__"]
                del obj_val["__class__"]
                self.new(eval(cls_name)(**obj_val))
        except FileNotFoundError:
            pass
