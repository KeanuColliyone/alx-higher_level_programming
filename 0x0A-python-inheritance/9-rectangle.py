#!/usr/bin/python3
class Rectangle(BaseGeometry):
    """Class representing a rectangle inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the Rectangle with width and height."""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

