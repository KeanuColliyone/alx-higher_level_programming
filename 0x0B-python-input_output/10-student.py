#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Defines a Student"""


    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""


        if attrs is None:
            return self.__dict__

        serializable_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                serializable_dict[attr] = getattr(self, attr)

        return serializable_dict
