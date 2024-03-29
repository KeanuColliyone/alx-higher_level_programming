#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Defines a Student"""


    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        serializable_dict = {}
        attributes = self.__dict__


        for key, value in attributes.items():
            if isinstance(value, (str, int)):
                serializable_dict[key] = value

        return serializable_dict
