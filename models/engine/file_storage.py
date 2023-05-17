#!/usr/bin/python3

import json
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User



class FileStorage:
    __file_path = "data_file.json"
    __objects = {}
    __classes = {'BaseModel': BaseModel, 'User': User, 'State': State, "Amenity": Amenity, "City": City, "Place": Place, "Review": Review}

    def all(self):
        return __class__.__objects
    
    def new(self, obj):
        key_str = "{}.{}".format(obj.__class__.__name__, obj.id)
        __class__.__objects[key_str] = obj

    def save(self):
        with open(__class__.__file_path, "w") as myobj:
            temp = __class__.__objects
            for k, v in temp.items():
                temp[k] = v.to_dict()
            json.dump(temp, myobj, indent=2)

    def reload(self):
        if os.path.isfile(__class__.__file_path):
            with open(__class__.__file_path, "r") as myobj:
                temp = json.load(myobj)
                for key, value in temp.items():
                    if key.split(".")[0] in __class__.__classes:
                        __class__.__objects[key] = __class__.__classes[key.split(".")[0]](**value)