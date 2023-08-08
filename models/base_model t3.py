#!/usr/bin/python3
"""
class BaseModel that defines all common
attributes/methods for other classes
take care of the initialization, serialization and
deserialization of your future instances
"""
import uuid
import datetime


class BaseModel:
    """
    class BaseModel that defines all common
    attributes/methods for other classes
    """

    def __init__(self):
        """ initialization """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ return a string [<class name>] (<self.id>) <self.__dict__> """
        return f"[{self.__class__.__name__}] ({self.id}) \
{self.__dict__}"

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """  returns a dictionary containing all keys/values of __dict__ of the instance """
        dictx = dict({"__class__": self.__class__.__name__}, **self.__dict__)
        dictx["created_at"] = dictx["created_at"].isoformat()
        dictx["updated_at"] = dictx["updated_at"].isoformat()
        return dictx
