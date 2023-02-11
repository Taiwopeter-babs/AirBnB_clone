#!/usr/bin/python3
"""
    This module defines a class `Review` that inherits from
    `BaseModel` and defines the Review attributes
"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place


class Review(BaseModel):
    """
        Review class

        Args:
            place_id(str): Place.id
            user_id(str): User.id
            text(str): review
    """

    place_id = ""
    user_id = ""
    text = ""
