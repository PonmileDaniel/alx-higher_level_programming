#!/usr/bin/python3
"""Defines a json"""
import json


def to_json_string(my_obj):
    """Return the json
    Args:
        my_obj: object
        
    """
    return json.dumps(my_obj)
