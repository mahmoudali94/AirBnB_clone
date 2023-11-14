#!/usr/bin/python3
"""
User.py module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User that inherits from BaseModel

    Attributes:
        email: The user email
        password: The User password
        first_name: The User first name
        last_name: The User last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
