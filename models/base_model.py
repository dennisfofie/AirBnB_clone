#!/usr/bin/python3
import uuid
from datetime import datetime
import models


"""
This is a base model for all this project
"""
class BaseModel():
    """ basemodel class attributes """
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = created_at

    def __init__(self, *args, **kwargs):
        """ initializes class """
        if kwargs:
            for key , value in kwargs.items():
                if key == "created_at" or key == "updated_at" and key != "__class__":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    key = value
        else:
            self.id = BaseModel.id
            self.created_at = BaseModel.created_at
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """ save the class and update the updated_at time """
        self.updated_at = datetime.now()
        models.storage.save()
                    

    def __str__(self):
        """ return string representation """
        return "{} {} {}".format(type(self).__name__, self.id, self.__dict__)
    
    def to_dict(self):
        """ create dictionary and asign values to a specific value """

        my_dict = dict(self.__dict__)

        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict

