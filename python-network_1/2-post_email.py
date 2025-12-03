#!/usr/bin/python3
"""Sends a POST request to a URL with an email
and displays the response body.
"""

from urllib import request
from urllib import parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare POST data
    data = parse.urlencode({"email": email}).encode("utf-8")

    # Send POST request
    req = request.Request(url, data=data, method="POST")
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
