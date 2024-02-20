#!/usr/bin/python3
"""Returns true otherwise false"""


def is_same_class(obj, a_class):
    """Civen class.

    Args:
        obj : The object to check.
        a_class : The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
    """
    if type(obj) == a_class:
        return True
    return False
