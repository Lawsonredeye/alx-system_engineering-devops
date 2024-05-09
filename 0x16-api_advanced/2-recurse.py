#!/usr/bin/python3
"""
Script that uses recursuion to fect a list of hot topics trending on
the users desired subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    use recursion to get the subreddits hot gist
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"user-agent":
               (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36"
                )}
    params = {
        "limit": 50,
        "after": after
    }

    # make request to the API
    try:
        r = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        # - check if the response was successful
        if r.status_code != 200:
            return None

        data = r.json()
        if "data" not in data or "children" not in data["data"]:
            return None
        posts = data["data"]["children"]
        for post in posts:
            new_post = post["data"]["title"]
            hot_list.extend(new_post)
        after = data["data"].get("after", None)
        if after is not None:
            return recurse(subreddit, hot_list, after=None)
        else:
            return hot_list
    except requests.RequestException:
        return None
