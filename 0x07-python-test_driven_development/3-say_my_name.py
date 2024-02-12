#!/usr/bin/python3
"""First name and last name"""


def say_my_name(first_name, last_name=""):
    """Print  My first name and last name
    
    Args:
        first_name: The first name.
        last_name: The last name default
        
    Raises:
        TypeError: If first and last name is not string 
    """
    
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
