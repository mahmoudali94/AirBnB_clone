#!/usr/bin/python3
"""
state.py module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State module that inherit from BaseModel

    Attributes:
        name: The name of the state
    """

    name = ""
