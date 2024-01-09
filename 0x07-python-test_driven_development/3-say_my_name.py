#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints the given first name and last name.

    Args:
    first_name (str): First name.
    last_name (str, optional): Last name. Defaults to an empty string.

    Raises:
    TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = ("My name is {} {}".format(first_name, last_name) if last_name
             else "My name is {}".format(first_name))
    print(full_name)

