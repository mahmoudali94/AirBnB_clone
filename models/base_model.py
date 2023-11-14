#!/usr/bin/python3
"""
BaseModel.py module
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
    class BaseModel that defines all common
    attributes/methods for other classes

    Methods:
        __init__(self, *args, **kwargs): The constructor
        of a BaseModel
        __str__(self): Return string representation of
        the instance
        save(self): Update the updated_at attribute
        and save the instance
        to_dict(self): Return a dictionary
        representation of the instance
    """

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or \
                            k == "updated_at":
                    date_f = datetime.fromisoformat(v)
                    setattr(self, k, date_f)
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
    # we can do type(self).__name__

    def save(self):
        """Update the updated_at attribute and
        save the instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation
        of the instance"""
        to_dict = self.__dict__.copy()
        new_dict = {}
        new_dict["__class__"] = type(self).__name__

        for k, v in to_dict.items():
            if k == "created_at" or k == "updated_at":
                new_dict[k] = datetime.isoformat(v)
            else:
                new_dict[k] = v
        return new_dict
