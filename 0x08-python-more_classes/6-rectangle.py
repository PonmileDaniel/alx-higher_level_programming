#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """Represent a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initalize a new Rectangle.
        Args:
            width: width of the new rectangle
            height: height of the new rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for i in range(self.__height):
            rec += "#" * self.__width + "\n"
        return rec.rstrip()

    def __repr__(self):
        """Return the string representation of the Rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print the message for every deletion."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
