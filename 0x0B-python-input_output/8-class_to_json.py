#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Converts an object to a JSON serializable dictionary."""
    serializable_dict = {}
    attributes = obj.__dict__

    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value

    return serializable_dict
