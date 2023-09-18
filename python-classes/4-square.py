#!/usr/bin/python3
"""This class defines Square"""


class Square:
    """this is a defining size and self as instance"""
    def __init__(self, size=0):

        @property
        def size(self):
            return self.__size

        def size(self, value):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        return self.__size**2
