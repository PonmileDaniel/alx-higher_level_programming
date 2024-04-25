#!/usr/bin/python3
'''The model for Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''height of the Rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''x of the rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        '''X for the int'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''y of the rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Area of a rectangle.'''
        return self.width * self.height

    def display(self):
        '''Print the string rep of the rec'''
        d = '\n' * self.y + \
            (' ' * self.x + "#" * self.width + '\n') * self.height
        print(d, end='')

    def __str__(self):
        '''Return string about the rectangle'''
        return f"[Rectangle] ({(self.id)}) {self.x}/{self.y} - " \
            f"{self.width}/{self.height}"
