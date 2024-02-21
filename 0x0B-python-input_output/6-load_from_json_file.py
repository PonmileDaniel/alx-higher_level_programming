#!/usr/bin/python3
"""Define json function"""
import json


def load_from_json_file(filename):
    """write an object to a text file with json"""
    with open(filename) as f:
        json.load(f)
