#!/usr/bin/python3
"""Defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """Check if the object inherits (directly or indirectly)
    from the specified class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
