#!/usr/bin/python3
"""Fetches a URL and displays the body of the response
handling HTTP errors if they occur.
"""

from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except error.HTTPError as e:
        print("Error code:", e.code)
