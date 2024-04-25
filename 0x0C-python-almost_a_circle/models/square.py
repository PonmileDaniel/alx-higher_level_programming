#!/usr/bin/python3
'''The model for square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A square Class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({(self.id)}) {self.x}/{self.y} - " \
            f"{self.width}"

    @property
    def size(self):
        '''Size of this square'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method that updates instance'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Update Instance attribute'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Return Dictionary representation of a rectangle'''
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
