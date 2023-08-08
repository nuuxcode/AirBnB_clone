#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel():
    """Define a BaseModel Class"""
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
    
    def __str__(self) -> str:
        """Returns the string representation of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the public instance updated_at"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """returns the dictionary representation of the instance"""
        dict_
        return self.__dict__