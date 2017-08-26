#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C1001
"""docstring"""
from time import sleep
import tweepy
from tweet_quijote import QuijoteTweet
from id_from_file import GettingId

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
    status_file = GettingId("last_status_id.txt")

    while True:
        id_status = status_file.get_id_from_file()
        tweet = quijote.get_quijote_tweet()
        api.update_status(tweet, in_reply_to_status_id=id_status)
        list_statuses = api.user_timeline(api.me().id)
        status_file.save_id_to_file(list_statuses[0].id)
        sleep(900)

if __name__ == "__main__":
    main()
