#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel():

    def __init__(self, *args, **kwargs):
        """Define a BaseModel Class"""
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    continue
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self) -> str:
        """Returns the string representation of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the public instance updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns the dictionary representation of the instance"""
        todict = self.__dict__
        todict["__class__"] = self.__class__.__name__
        todict["created_at"] = todict["created_at"].isoformat()
        todict["updated_at"] = todict["updated_at"].isoformat()
        return todict
