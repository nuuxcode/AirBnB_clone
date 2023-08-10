#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
#from models.base_model import BaseModel #avoid circular

class FileStorage:
    """ doc """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        id = obj.to_dict()["id"]
        className = obj.to_dict()["__class__"]
        keyName = className+"."+id
        FileStorage.__objects[keyName] = obj

    def save(self):
        filepath = FileStorage.__file_path
        data = dict(FileStorage.__objects)
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(filepath, 'w') as f:
            json.dump(data, f)
        
    def reload(self):
        filepath = FileStorage.__file_path
        data = FileStorage.__objects
        if os.path.exists(filepath):
            with open(filepath) as f:
                for key, value in json.load(f).items():
                    if "BaseModel" in key:
                        data[key] = BaseModel(**value)
                    if "User" in key:
                        data[key] = User(**value)
