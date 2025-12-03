#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using requests"""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.content

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
