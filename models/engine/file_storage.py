#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        var_name = obj.__class__.__name__
        self.__objects["{}.{}".format(var_name, obj.id)] = obj

    def save(self):
        o_dict = FileStorage.__objects
        obj_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_nme = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_nme)(**o))
        except FileNotFoundError:
            return
