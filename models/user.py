#!/usr/bin/python3

"""
User class that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Class that defines attributes for an user, sets all of them to empty """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
