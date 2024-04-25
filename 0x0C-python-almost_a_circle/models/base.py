#!/usr/bin/python3
'''For base class'''
from json import dumps, loads


class Base:
    '''Representation of the base of the oop'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Construct'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
    @staticmethod
    def to_json_string(list_dictionaries):
        '''Json return'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
