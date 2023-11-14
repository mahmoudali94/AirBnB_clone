#!/usr/bin/python3
"""
place.py module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place module that inherit from the baseModel

    Attributes:
        city_id: The Place id
        user_id: The Place user id
        name: The Place name
        description: The Place description
        number_rooms: The Place number of rooms
        number_bathrooms: The Place number of bathrooms
        max_guest: The Place max guest
        price_by_night: The Place price per night
        latitude: The Place latitude
        longitude: The Place longitude
        amenity_ids: The Place amenity ids
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
    amenity_ids = ""
