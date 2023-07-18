#!/usr/bin/python3
"""define class base"""


class Base:
    """the base of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization function

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        import json
        return json.dumps(list_dictionaries)
