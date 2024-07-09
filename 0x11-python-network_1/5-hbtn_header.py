#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.header['X-Request-Id'])
    except:
        pass
