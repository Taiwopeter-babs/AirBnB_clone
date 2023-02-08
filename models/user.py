#!/usr/bin/python3
"""
    This module defines a class `User` that inherits from
    `BaseModel` and defines the users' attributes
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        User class

        Args:
            email(str): email of user
            password(str): password of user
            first_name(str): first name of user
            last_name(str): last name of user

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
