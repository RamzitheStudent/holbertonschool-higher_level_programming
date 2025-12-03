#!/usr/bin/python3
"""Uses GitHub API with Basic Authentication to display the user id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]  # Personal access token

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    print(response.json().get("id"))
