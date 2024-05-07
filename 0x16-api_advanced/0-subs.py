#!/usr/bin/python3
"""
Function that queries reddit api and returns tota number of subscribers
using the requests library and the sys.args lib
"""

import requests


def number_of_subscribers(subreddit):
    """
    This function returns the total number of subscribers that a subreddit has
    and returns 0 if the subreddit doesn't exists

    Args:
        param:str : name of subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about/.json"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        for key, value in data.items():
            if key == "data":
                for k, v in value.items():
                    if k == "subscribers":
                        return v
    else:
        return 0
