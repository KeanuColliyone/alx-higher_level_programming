#!/usr/bin/python3
"""This module defines a Square class representing a geometric square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initializes a Square instance with size.

        Args:
            size (int or float, optional): The size of the square (default 0).
        Raises:
            TypeError: If size is not a number (int or float).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Checks if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks if the area of one square is less than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if the area of one square is less than or equal to the other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checks if the area of one square is greater than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if the area of one square is greater than or equal to the other."""
        return self.area() >= other.area()
