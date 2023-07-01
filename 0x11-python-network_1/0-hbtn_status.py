#!/usr/bin/python3
import urllib.request
"""script that fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    my_url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(my_url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf-8'))
