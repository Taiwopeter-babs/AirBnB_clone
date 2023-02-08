#!/usr/bin/python3
"""
    This module defines a class `Amenity` that inherits from
    `BaseModel` and defines the amenities
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Amenity class

        Args:
            name(str): amenities in Airbnb
    """

    name = ""
