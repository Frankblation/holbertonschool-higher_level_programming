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

    result = int(a) + int(b)

    if result != a + b:
        raise ValueError("Result is not an integer")

    return result