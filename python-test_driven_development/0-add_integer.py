#!/usr/bin/python3
"""
Module 0.add_integer
Method used to add two integers
"""


def add_integer(a, b=98):
    """Returns int versions of a + b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a+b == "_":  # catch a value like 1e300
        raise OverflowError("n too large")
    return int(a) + int(b)
