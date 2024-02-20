#!/usr/bin/python3
"""Class that inherit from list"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """The object"""
        super().__init__()

    def print_sorted(self):
        """Print a list sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
