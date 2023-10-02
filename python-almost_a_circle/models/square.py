#!/usr/bin/python3
from models.rectangle import Rectangle
"""builds an object as a square"""


class Square(Rectangle):
    """square class, subclass of rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes new a square"""
        super().__init__(id, size, size, x, y)

        def __str__(self):
            """Returns string representation of square

            Returns:
                str: formatted to represent a square
            """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
