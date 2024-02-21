#!/usr/bin/python3
"""Define json function"""


def class_to_json(obj):
    """Returnthe dict"""
    return obj.__dict__
