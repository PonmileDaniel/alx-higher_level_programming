#!/usr/bin/python3
"""Modules for add_integer method"""


def add_integer(a, b=98):
    """Adds two integer
    
    Args:
        a: This is first number
        b: 98 by default
    Error:
        TypeError: if a , b is not an integer
    Return:
        The sum of two integer
    """
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
    