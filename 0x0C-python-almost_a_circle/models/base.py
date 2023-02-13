#!/usr/bin/python3
"""Base Class"""


import json
import os
import csv
import time
from random import randrange


class Base:
    """Parent Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation
            of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
            of list_objs to a file"""

        file = "{}.json".format(cls.__name__)

        with open(file, "w") as file_obj:
            file_obj.write('[')
            for i in range(len(list_objs)):
                file_obj.write(Base.to_json_string(
                    list_objs[i].to_dictionary()))
                if i != len(list_objs) - 1:
                    file_obj.write(', ')
            file_obj.write(']')

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation"""

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of intances"""

        file = "{}.json".format(cls.__name__)
        instances = []
        if os.path.isfile(file):
            with open(file, "r", endcoding="utf-8") as file_obj:
                for dictionary in cls.from_json_string(file_obj.read()):
                    instances.append(cls.create(**dictionary))
        return instances
