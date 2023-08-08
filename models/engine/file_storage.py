#!/usr/bin/python3
import json
import os

class FileStorage():
    """ doc """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        id = obj.id
        className = obj.__class__
        keyName = className+"."+id
        setattr(FileStorage.__objects, keyName, obj)

    def save(self):
        filepath = FileStorage.__file_path
        data = FileStorage.__objects
        with open(filepath, 'w') as f:
            json.dump(data, f)

    def reload(self):
        filepath = FileStorage.__file_path
        if os.path.exists(filepath):
            with open(filepath) as f:
                FileStorage.__objects = json.load(f)
