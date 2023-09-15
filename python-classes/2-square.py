#!/usr/bin/python3
"""This class defines Square"""


class Square:
    """this is a defining size and self as instance"""
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
