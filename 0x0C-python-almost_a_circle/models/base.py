#!/usr/bin/python3
'''For base class'''


class Base:
    '''Representation of the base of the oop'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Construct'''
        if id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
