#!/usr/bin/python3
"""Define a function"""


def write_file(filename="", text=""):
    """Write a string to utf-8"""
    with open(filename, "r", encoding="utf-8") as f:
        return f.write(text)
