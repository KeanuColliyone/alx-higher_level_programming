#!/usr/bin/python3
"""This module defines a Square class representing a geometric square."""


class Square:
    """Represents a square with private instance attributes: size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes an instance of the Square class with optional size and position.

        Args:
            size (int, optional): The size of the square (default 0).
            position (tuple, optional): The position of the square (default (0, 0)).
        Raises:
            TypeError: If size is not an integer or if position is not a tuple of two positive integers.
            ValueError: If size is less than 0 or if position contains non-positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with type and value validation.

        Args:
            value (tuple): The position to set.
        Raises:
            TypeError: If value is not a tuple of two positive integers.
            ValueError: If position contains non-positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(i < 0 for i in value):
            raise ValueError("position must contain positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' character at the specified position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
