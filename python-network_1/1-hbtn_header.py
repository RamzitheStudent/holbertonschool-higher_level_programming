#!/usr/bin/python3
"""Fetches a URL and displays the value of the X-Request-Id header"""

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        headers = response.info()
        print(headers.get("X-Request-Id"))
