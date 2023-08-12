#!/usr/bin/python3
"""base model of our airBnB"""

from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    """Define BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel object."""
        pass

    def __str__(self):
        """string method that return descriptor of the object"""
        pass

    def save(self):
        """save method that save time update and update"""
        pass

    def to_dict(self):
        """to_dict method that get an prepared dict"""
        pass
