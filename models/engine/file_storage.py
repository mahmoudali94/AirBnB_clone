#!/usr/bin/python3
"""
FileStorage.py module
"""
from os import path
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    Handles serialization and
    deserialization to a JSON file.

    Attibutes:
        __file_path: private class attribute
        contain file name
        __objects: private class attribute to store
        all objects by <class name>.id
        class_name: Class Attribute list
        classes in Airbnb Project.

    Methods:
        all(self): Return the dictionary __objects
        new(self, obj): Set in __objects
        the obj with key <obj class name>.id
        save(self): Serialize __objects
        to the JSON file (path: __file_path)
        reload(self): Deserialize the JSON
        file (path: __file_path) to __objects
    """
    __file_path = "file.json"
    __objects = {}
    class_name = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with
        key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__,
                             obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the
        JSON file (path: __file_path)"""
        new_dict = {}

        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w",
                  encoding="utf-8") as save_file:
            json.dump(new_dict, save_file)

    def reload(self):
        """Deserialize the JSON file
        (path: __file_path) to __objects"""

        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path,
                      "r") as read_file:
                file_data = json.load(read_file)
            for key, val in file_data.items():
                dict_class = val["__class__"]
                # dict_class, _ = key.split(".")
                class_n = FileStorage.class_name[dict_class]
                if dict_class == class_n.__name__:
                    FileStorage.__objects[key] = class_n(**val)
