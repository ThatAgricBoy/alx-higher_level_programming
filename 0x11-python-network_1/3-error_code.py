#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""


import urllib.request
import sys
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response.read()
    except HTTPError as e:
        print(e.code)
    else:
        print(response.decode('utf-8'))
