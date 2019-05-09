#!/usr/bin/python3
"""
Queries Reddit API and returns a list containing the titles of all hot
articles for a given subreddit
"""


import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit
    """
    url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    headers = {'user-agent': 'custom'}
    try:
        r = requests.get(url, headers=headers,
                         allow_redirects=False, params={'after': after}).json()
        data_list = r.get("data").get("children")
        after = r.get("data").get("after")
        for data in data_list:
            hot_list.append(data.get("data").get("title"))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return (None)
