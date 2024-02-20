#!/usr/bin/python3
"""Define a function that returns the list attribute"""


def lookup(obj):
    """Return list of object availables.
    Args: object to lookup attribute and method
    Returns:
    list of available attributes and method
    """
    return(dir(obj))
