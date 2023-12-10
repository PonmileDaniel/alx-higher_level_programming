#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = a_dictionary.copy()
    for i, value in a_dictionary.items():
        newdic[i] = value * 2
    return (newdic)
