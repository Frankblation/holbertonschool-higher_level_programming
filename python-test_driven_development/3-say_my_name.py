#!/usr/bin/python3
"""
Prints name in the format first name last name
"""


def say_my_name(first_name, last_name=""):
    """_summary_

    Args:
        first_name (st): first name
        last_name (str, optional): last name. Defaults to "".
    """
    if not isinstance(first_name, str):
        raise
    TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
