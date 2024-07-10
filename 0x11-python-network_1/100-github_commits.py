#!/usr/bin/python3
"""A python script that takes 2 arguments in order to solve
    multiple technical challenges
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)
    commits = response.json()

    for commit in range(10):
        sha = commits[commit].get("sha")
        author_name = commits[commit].get("commit").get("author").get("name")
        print(f"{sha}: {author_name}")
