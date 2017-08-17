#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Execution Bot"""
import tweepy
from bot import MakingActions
from PyTweListener import PyTweListener


def main():
    """The bot is living"""
    consumer_key = "GvyW21D2vYcP6VU1MALnpqa5t"
    consumer_secret = "e6njXmtk2CtPqSVU2PNs4neBEUkHrzHHse7eK9tOSOMvwNxVD5"

    access_token = "895306836345323520-jHuEuGn8CHTLhEjJ9T5MCnsxUXFE8nq"
    access_token_secret = "OdVrxNhDjgvTrOvCV1MJd5VuaK6bz4I6szyz8SaLZl0Qa"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    listener = PyTweListener()
    stream = tweepy.Stream(api.auth, listener)
    # filtrando tweets por un patrón
    # stream.filter(track=["ultra kek 0 name"])
    stream.userstream()
if __name__ == "__main__":
    main()
