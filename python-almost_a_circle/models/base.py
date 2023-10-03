#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """Initialize a new instance of the Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns The Json String Representation of List_Dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        if type(list_dictionaries) is list:
            for dictionaries in list_dictionaries:
                if type(dictionaries) is not dict:
                    return "[]"
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string,list_objs to a file in JSON format.
        """
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
            if not isinstance(object, cls):
                raise
        TypeError(f"objects in list_objs must be instances of {cls.__name__}")
        list_objs.append(object.to_dictionary())
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))
