#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Execution Bot"""
import tweepy
from bot import MakingActions
from PyTweListener import PyTweListener


def main():
    """The bot is living"""
    consumer_key = ""
    consumer_secret = ""

    access_token = "895306836345323520-"
    access_token_secret = ""

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
