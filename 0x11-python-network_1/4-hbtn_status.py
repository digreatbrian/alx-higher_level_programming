#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
using GET
"""
import requests

if __name__ == '__main__':
    url = "https://intranet.alxswe.com/status"
    status = requests.get(url).text
    print("Body response:")
    print("\t- type: {}".format(type(status)))
    print("\t- content: {}".format(status))
