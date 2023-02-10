"""
a module that defines all common at
"""
import uuid
import datetime
import json


class BaseModel:

    """
    creates a string unique user id
    """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f'[{self.__class__.__name__}] {self.id} {self.__dict__}'

    def to_dict(self, *args, **kwargs):
        dict_info = self.__dict__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        dict_info['__class__'] = self.__class__.__name__
        if kwargs is not {}:
            for key in kwargs:
                kwargs['__class__'] = dict_info['__class__']
                dict_info['__class__'] = self.__class__.__name__
                setattr(self, key, kwargs[key])
        return dict_info





