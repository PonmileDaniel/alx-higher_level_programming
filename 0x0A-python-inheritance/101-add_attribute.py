#!/usr/bin/python3
"""New attribute"""


def add_attribute(obj, name, value):
    """Function that adds a new attribute."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
