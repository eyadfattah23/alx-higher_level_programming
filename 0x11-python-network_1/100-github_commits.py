#!/usr/bin/python3
'''script that lists last 10 commits of a repository
repository is given in argv[1]
user is given in argv[2]'''

import sys
import requests

if __name__ == '__main__':
    USERNAME = sys.argv[2]
    REPO = sys.argv[1]
    TOKEN = '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'

    url = f" https://api.github.com/repos/{USERNAME}/{REPO}/commits"

    data = {"Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"}

    req = requests.get(url, headers=data)
    response_json = req.json()
    i = 0
    for commit in response_json:
        if i > 9:
            break
        print(commit.get('sha') + ': ' + commit['commit']['author']['name'])
        i += 1
