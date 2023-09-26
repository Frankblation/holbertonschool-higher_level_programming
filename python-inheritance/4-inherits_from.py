#!/usr/bin/python3
""" Returns True if the object is an instance of specified class;
    otherwise, returns False.
"""


def inherits_from(obj, a_class):
    """
    Args:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    bool: True if obj is an subclass of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
