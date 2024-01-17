#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:
            upper_case = chr(ord(char) - 32)
            print("{}".format(upper_case), end="")
        else:
            print("{}".format(char), end="")
    print()