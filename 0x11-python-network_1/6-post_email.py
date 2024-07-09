#!/usr/bin/python3
"""Python script that takes in a Url and an email"""
import requests
import sys


if __name__ == "__main__":
    b = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(b.text)
