#!/usr/bin/python3
"""a function that queries the Reddit API and prints
the titles of the first hot 10 posts listed for a given subreddit.

If an invalid subreddit is given, the function prints None.
"""
import requests


def top_ten(subreddit):
    """Prints the first hot 10 posts listed for a given subreddit"""

    if subreddit is None or not isinstance(subreddit, str):
        print(None)

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get("data").get("children")

            for datum in data:
                print(datum.get("data").get("title"))
        else:
            print(None)
    except Exception:
        print(None)
