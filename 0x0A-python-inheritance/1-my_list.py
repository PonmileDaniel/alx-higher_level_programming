#!/usr/bin/python3
"""Class that inherit from list"""


class MyList(list):
    def print_sorted(self):
        """Print a list sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
