#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_key = sorted(a_dictionary.keys())
    for key in sorted_key:
        value = a_dictionary[key]
        print("{}: {}".format(key, a_dictionary.get(key)))
