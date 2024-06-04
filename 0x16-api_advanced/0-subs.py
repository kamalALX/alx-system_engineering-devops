#!/usr/bin/python3
""" queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers for a given subreddit. """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Morocco"
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json().get('data')
        subscribers = data.get('subscribers')
        return subscribers
    except (KeyError, requests.RequestException):
        return 0
