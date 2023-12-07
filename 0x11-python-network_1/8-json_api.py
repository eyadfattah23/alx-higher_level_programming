#!/usr/bin/python3
'''
 script that takes in a letter
 and sends a POST request to http://0.0.0.0:5000/search_user
 with the letter as a parameter.'''

import sys
import requests

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        qv = sys.argv[1]
    else:
        qv = ""
    req = requests.post(url, data={'q': qv})
    try:
        respones_json = req.json()
        if respones_json:
            print(f"[{respones_json.get('id')}] {respones_json.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
