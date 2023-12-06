#!/usr/bin/python3
'''script that fetches https://alx-intranet.hbtn.io/status'''

import urllib.request
import urllib.parse

if __name__ == "__main__":
    with urllib.request.\
            urlopen('https://alx-intranet.hbtn.io/status') as response:
        print("Body response:")
        html = response.read()
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('UTF-8')}")
