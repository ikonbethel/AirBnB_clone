#!/usr/bini/python3
"""
Module FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """Serializes instances of JSON file and JSON file to instances
    Class Attributes:
        __file_path - string that contains path to JSON file
        __objects - dictionary that stores all objects
    Methods:
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class_name.id
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
        """
        dic = {}

        for key, val in self.__objects.items():
            if isinstance(val, dict):
                dic[key] = val
            else:
                dic[key] = val.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(dic, f)

    def reload(self):
        """If json file exists the deserialize it back to instances
        """
        try:
            with open(self.__file_path, 'r') as f:
                dic = json.load(f)
                for key, val in dic.items():
                    cls = val['__class__']
                    obj = eval(cls)(**val)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
