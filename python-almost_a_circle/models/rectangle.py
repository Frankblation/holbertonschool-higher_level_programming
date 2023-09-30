#!/usr/bin/python3
"""This module defines the Rectangle class."""
from models.base import Base

class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): The ID of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > than 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > than 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= to 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= to 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle with '#' characters."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)