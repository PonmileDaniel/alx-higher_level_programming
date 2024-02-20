#!/usr/bin/python3
"""Returns true otherwise false"""


def is_same_class(obj, a_class):
    """
    obj: The object to check
    a_class: The class to compare against.
    """
    if type(obj) == a_class:
        return True
    return False
