#!/usr/bin/python3
"""
    This module defines a class `City` that inherits from
    `BaseModel` and defines the city's attributes
"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """
        City class

        Args:
            state_id(str): State.id
            name(str): name of city
    """
    
    state_id = ""
    name = ""
