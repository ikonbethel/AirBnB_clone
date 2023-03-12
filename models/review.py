#!/usr/bin/python3
"""
Module Review class
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
