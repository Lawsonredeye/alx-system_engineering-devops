#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests

headers = {"user-agent": (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)}


def top_ten(subreddit):
    """
    This function returns the response of a reddit on the latest
    hot posts
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()

        posts = data["data"]["children"]

        for post in posts[:10]:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)
