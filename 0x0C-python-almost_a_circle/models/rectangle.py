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
        #self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Height of the Rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        #self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x of the rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        #self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''y of the rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        #self.validate_integer("y", value)
        self.__y = value

    def area(self):
        '''Computing the area of rectangle'''
        return self.width * self.height
