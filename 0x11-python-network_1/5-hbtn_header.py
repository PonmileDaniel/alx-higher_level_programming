#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except requests.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)
