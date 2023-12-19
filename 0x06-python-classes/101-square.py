#!/usr/bin/python3
"""This module defines a Square class representing a geometric square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with size and position.

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
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
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

    def __str__(self):
        """Represents the square when printed."""
        string_representation = ""
        if self.__size == 0:
            return string_representation
        else:
            for _ in range(self.__position[1]):
                string_representation += "\n"
            for _ in range(self.__size):
                string_representation += " " * self.__position[0] + "#" * self.__size + "\n"
            return string_representation.strip()
