#!/usr/bin/python3
"""Define a function"""


def write_file(filename="", text=""):
    """Write a string to utf-8"""
    n = 0
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            n += 1
    return n
