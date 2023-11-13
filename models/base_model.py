#!/usr/bin/python3
"""Defines a BaseModel class"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    Declares the BaseModel
    Acts as a parent class of all other classes in the project
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance
        """
        form = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "created_at":
                    self.created_at = datetime.strptime(v, form)
                elif k == "my_number":
                    self.my_number = v
                elif k == "updated_at":
                    self.updated_at = datetime.strptime(v, form)
                elif k == "name":
                    self.name = v
        else:
            self.id = uuid.uuid4().hex
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string format of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Saves an instance
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts an object to a dictionary
        """
        obj_dict = self.__dict__.copy()

        obj_dict['__class__'] = self.__class__.__name__

        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
