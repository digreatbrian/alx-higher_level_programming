#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository
"""
import requests
from sys import argv

if __name__ == "__main__":
    username, repo = argv[1], argv[2]
    url = "https://api.github.com/repos/{}/{}/commits"
    url = url.format(username, repo)
    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            sha = commits[i].get("sha")
            name = commits[i].get("commit").get("author").get("name")
            print("{}: {}".format(sha, name))
    except IndexError:
        pass
