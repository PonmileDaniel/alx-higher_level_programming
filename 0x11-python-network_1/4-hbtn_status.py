#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    b = response.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(b), b))
