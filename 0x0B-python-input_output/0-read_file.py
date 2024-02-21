#!/usr/bin/python3
"""Define a text file"""


def read_file(filename=""):
    """Print the content"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
