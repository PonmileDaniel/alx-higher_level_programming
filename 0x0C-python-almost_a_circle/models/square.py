#!/usr/bin/python3
"""Module for the square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initalize a SQUARE"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string rep of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
