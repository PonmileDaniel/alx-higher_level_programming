#!/usr/bin/python3
"""Returns true otherwise false"""


def is_same_class(obj, a_class):
    """Checking if an object is exactly an instance
    
    Args:
        obj: The object to check
        a_class: The class to compare against.
    Returns:
        if the object is the same true otherwise false 
    """
    if type(obj) == a_class:
        return True
    return False
