"""
flow of serialization and deserialization
"""
import json


class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        self.__file_path = json.dumps(self.__objects)

