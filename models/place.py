#!/usr/bin/python3
"""
    This module defines a class `Place` that inherits from
    `BaseModel` and defines the Airbnb place's attributes
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City

class Place(BaseModel):
    """
        Place class of residence

        Args:
            city_id(str): City.id
            user_id(str): User.id
            name(str): name of Airbnb residence
            description(str): description of Airbnb residence
            number_rooms(int): Number of rooms in Airbnb residence
            number_bathrooms(int): Number of bathrooms in Airbnb residence
            max_guest(int): Maximum guests residence can accomodate
            price_by_night(int): Price of residence per night
            latitude(float): latitudinal location of residence
            longitude(float) longitudinal location of residence
            amenity_ids(list): Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
