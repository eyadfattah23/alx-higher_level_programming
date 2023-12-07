#!/usr/bin/python3
'''script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id'''
import sys
import requests

if __name__ == '__main__':
    USERNAME = sys.argv[1]
    YOUR_TOKEN = sys.argv[2]
    url = f"https://api.github.com/users/{USERNAME}"

    data = {"Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {YOUR_TOKEN}",
            "X-GitHub-Api-Version": "2022-11-28"}

    req = requests.get(url, headers=data)
    response_json = req.json()
    id = response_json.get('id')
    print(id)
