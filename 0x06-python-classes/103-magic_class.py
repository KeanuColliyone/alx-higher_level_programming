#!/usr/bin/python3
"""This module defines a MagicClass with similar functionality to the provided bytecode."""


import math

class MagicClass:
    """Represents a MagicClass with similar functionality to the provided bytecode."""
    
    def __init__(self, radius=0):
        """Initializes a MagicClass instance with a radius attribute."""
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        """Retrieves the radius of the circle."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Sets the radius of the circle."""
        if not isinstance(value, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = value

    def area(self):
        """Calculates and returns the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates and returns the circumference of the circle."""
        return 2 * math.pi * self.__radius
