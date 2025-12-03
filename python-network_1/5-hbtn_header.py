#!/usr/bin/python3
"""Fetches a URL and displays the value of X-Request-Id
in the response headers.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
