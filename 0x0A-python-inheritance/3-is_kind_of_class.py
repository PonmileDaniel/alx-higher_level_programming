#!/usr/bin/python3
"""Define a class"""


def is_kind_of_class(obj, a_class):
    """Return true if the object is an instance or false otherwise"""
    if isinstance(obj, a_class):
        return True
    return False
