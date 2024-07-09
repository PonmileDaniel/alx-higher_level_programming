#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys


if __name__ == "__main__":
    r = sys.argv[1]
    response = requests.get(r)
print(response.headers.get('X-Request-Id'))
