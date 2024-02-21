#!/usr/bin/python3
"""Define a class."""


class MyInt(int):
    """Int operator == !=."""
    
    def __eq__(self, value):
        """Override operator"""
        return self.real != value

    def __ne__(self, value):
        """override != operator"""
        return self.real == value
