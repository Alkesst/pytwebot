#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Execution Bot"""
import tweepy
from PyTweListener import PyTweListener


def main():
    """The bot is living"""
    consumer_key = ""
    consumer_secret = ""

    access_token = "-"
    access_token_secret = ""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)


    listener = PyTweListener(api)
    stream = tweepy.Stream(api.auth, listener)
    timeline = raw_input("You want to see your home timeline? ")
    if timeline == "yes":
        stream.userstream()
    # filtrando tweets por un patrón
    # stream.filter(track=["ultra kek 0 name"])
    else:
         filtr = []
        data = raw_input("Add words to filter. type end to finish the list. ")
        while data != 'end':
            filtr.append(data)
            data = raw_input()
        stream.filter(track=filtr)
if __name__ == "__main__":
    main()
