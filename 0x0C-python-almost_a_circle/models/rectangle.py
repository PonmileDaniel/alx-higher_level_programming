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

    # def update(self, *args):
    #     '''Update instance of Attribute'''
    #     if len(args) >= 1:
    #         self.id = args[0]
    #     if len(args) >= 2:
    #         self.width = args[1]
    #     if len(args) >= 3:
    #         self.height = args[2]
    #     if len(args) >= 4:
    #         self.x = args[3]
    #     if len(args) >= 5:
    #         self.y = args[4]

    def update(self, *args, **kwargs):
        '''Update instance of Attribute'''
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[2] if len(args) >= 3 else self.height
            self.x = args[3] if len(args) >= 4 else self.x
            self.y = args[4] if len(args) >= 5 else self.y
        else:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.width)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
