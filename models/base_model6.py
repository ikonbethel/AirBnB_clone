#!/usr/bin/python3
"""
Module BaseModel class
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """Base class for Airbnb clone project
    Methods:
        __inint__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """Initializes attributes
        Attributes:
            id - assigned with an uuid
            created_at - assigned with datetime
            updated_at - assined with date time
        """
        if kwargs:
            dt = "%Y-%m-%dT%H:%M:%S.%f"
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(val, dt)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(val, dt)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns the object
        """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys and values of
        __dict__ of the instance. A new key "__class__" is also added
        """
        dic = {}
        for key, val in self.__dict__.items():
            dic[key] = val
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
