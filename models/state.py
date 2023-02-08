#!/usr/bin/python3
"""
    This module defines a class `State` that inherits from
    `BaseModel` and defines the state attributes
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        State class

        Args:
            name(str): name of state
    """

    name = ""
