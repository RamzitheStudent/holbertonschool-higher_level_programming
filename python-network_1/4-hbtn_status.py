#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using urllib and prints the body as a string"""

from urllib import request
import sys

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        body = response.read().decode("utf-8")

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
