#!/usr/bin/python3
"""
class BaseModel that defines all common
attributes/methods for other classes
take care of the initialization, serialization and
deserialization of your future instances
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    class BaseModel that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialization of BaseModel Class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """Returns the string representation of an instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        """update the public instance updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """returns the dictionary
        representation of the instance"""
        todict = dict(self.__dict__)
        todict["__class__"] = self.__class__.__name__
        if not isinstance(todict["created_at"], str):
            todict["created_at"] = todict["created_at"].isoformat()
        if not isinstance(todict["updated_at"], str):
            todict["updated_at"] = todict["updated_at"].isoformat()
        return todict
