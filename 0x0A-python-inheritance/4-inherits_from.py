#!/usr/bin/python3
"""The object of an instance of a class"""


def inherits_from(obj, a_class):
    """Check if an object is inherited of a class"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
