#!/usr/bin/python3
"""builds an object as a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class, subclass of rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes new a square
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
            """
        super().__init__(id, size, size, x, y)

    def __str__(self):
        """Returns string representation of square"""
        return "[Square] \
            ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
