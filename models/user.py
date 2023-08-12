#!/usr/bin/python3
""" Doc Here """
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
