#!/usr/bin/python3
#!/usr/bin/python3#!/usr/bin/python3
""" Returns True if the object is an instance of specified class;
    otherwise, returns False.
"""


def is_same_class(obj, a_class):
    """
    Args:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    bool: True if obj is an subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class) and not type(obj) is a_class
