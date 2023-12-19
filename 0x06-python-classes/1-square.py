#!/usr/bin/python3
class Square:
    """Represents a square with a private instance attribute: size."""
    
    def __init__(self, size):
        """Initializes an instance of the Square class with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
