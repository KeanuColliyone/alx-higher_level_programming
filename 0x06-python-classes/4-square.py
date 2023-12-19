#!/usr/bin/python3
"""This module defines a Square class representing a geometric square."""


class Square:
    """Represents a square with a private instance attribute: size."""

    def __init__(self, size=0):
        """Initializes an instance of the Square class with an optional size.

        Args:
            size (int, optional): The size of the square (default 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value validation.

        Args:
            value (int): The size to set.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
