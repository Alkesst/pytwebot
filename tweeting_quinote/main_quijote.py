#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C1001
"""docstring"""
from time import sleep
import tweepy
from tweet_quijote import QuijoteTweet

def main():
    """Module"""
    consumer_key = ""
    consumer_secret = ""

    access_token = ""
    access_token_secret = ""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    quijote = QuijoteTweet("quijote.txt", "kek.txt")

    while True:
        tweet = quijote.get_quijote_tweet()
        api.update_status(tweet)
        sleep(1800)

if __name__ == "__main__":
    main()
