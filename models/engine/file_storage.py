#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """ 
    FileStorage - The storage class of our airbnb project
    @__file_path: The json file
    @__object: dictionary representation of our json data
    """
    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """ returns our dictionary object """
        return FileStorage.__objects

    def new(self, obj):
        """
        checks if the object which is been created exit add assigning our dictiionary with the id as key """

        if obj:
            key = "{} {}".format(type(self).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        1. looks for the key / pairs in our __object dictionary
        2. converting the value to dictionary using the to_dict() method in BaseModel
        3. open our file in w mode and converts our dictionary to json strings using the dump
        """
        data = {}
        for key , value in self.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path , mode="w", encoding="utf-8") as f:
            json.dump(data, f)
    """
    printing the json string to see the data mapping
        for line in f:
            print(line)
    """
    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        class_elements = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return class_elements

    def reload(self):
        """
        reloading from the json string to object i.e dictionary
        """
        if not self.__file_path:
            return
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                data = json.load(f)

                for key , value in data.items():
                    my_object = eval(value["__class__"])(**value)
                    self.__objects[key] = my_object
        except FileNotFoundError:
            pass

