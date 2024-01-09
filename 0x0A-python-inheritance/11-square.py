#!/usr/bin/python3
"""Defines a class Square thta inherits from Rectangle"""


class Square(Rectangle):
    """Class representing a square inheriting from Rectangle."""


    def __init__(self, size):
        """Initialize the Square with size."""
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)


    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
