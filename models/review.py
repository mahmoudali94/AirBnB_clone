#!/usr/bin/python3
"""
review.py module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review module that iherit from the BaseModel

    Attribues:
        place_id: The review plcae id
        user_id: The review user id
        text: The review  text
    """

    place_id = ""
    user_id = ""
    text = ""
