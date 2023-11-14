#!/usr/bin/python3
"""
city.py module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City module that inherit from the BaseModel

    Attributes:
        state_id: The city id
        name: The city name
    """

    state_id = ""
    name = ""
