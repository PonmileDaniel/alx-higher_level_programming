#!/usr/bin/python3
"""creating a file for rectangle"""
from models.base import Base


class Rectangle(Base):
    """Creating a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width: The width of a new rectangle
            height: The height of a rectangle
            x: The x coordinate of the rectangle
            y: The y coordinate of the rectangle
        Raises:

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
        # if len(args) > 0:
        #     self.id = args[0]
        # if len(args) > 1:
        #     self.width = args[1]
        # if len(args) > 2:
        #     self.height = args[2]
        # if len(args) > 3:
        #     self.x = args[3]
        # if len(args) > 4:
        #     self.y = args[4]

    def to_dictionary(self):
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
