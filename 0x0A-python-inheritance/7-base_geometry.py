#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """Class representing a base geometry."""

    def area(self):
        """Raises an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """Validates the value and raises exceptions if conditions are not met."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0"
