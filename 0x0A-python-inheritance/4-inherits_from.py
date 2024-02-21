#!/usr/bin/python3
"""The object of an instance of a class"""


def inherits_from(obj, a_class):
    """Check if an object is inherited of a class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
