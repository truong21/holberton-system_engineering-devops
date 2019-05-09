#!/usr/bin/python3
"""
Queries Reddit API and returns top ten titles for a subreddit
"""


import json
import requests


def top_ten(subreddit):
    """ return top ten titles for a subreddit """
    title_list = []
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'custom'}
    try:
        r = requests.get(url, headers=headers, allow_redirects=False).json()
        data_list = r.get("data").get("children")
        for data in data_list:
            title_list.append(data.get("data").get("title"))
        for i in range(10):
            print(title_list[i])
    except Exception:
        print("None")
