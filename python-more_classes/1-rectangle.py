#!/usr/bin/python3
"""this is a class named Rectangle"""


class Rectangle:
    """Rectangle class defined by  with height"""

    def __init__(self, width=0, height=0):
        """initializes a Rectangle instance

        Args:
            width (int, optional): Defaults to 0.
            height (int, optional): Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for with of triangle

        Args:
            value (int): the int value of witdth

        Raises:
            TypeError:  width must be an integer
            ValueError:  width must be greater or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """the setter for the height of a rectangle

        Args:
            value (int): value of height of the rectangle

        Raises:
            TypeError: height must be an integer
            ValueError: height must be greater than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
