#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made with python 2.7
# @Alkesstt at twitter. Alkesst @ telegram and GitHub.
import json
import tweepy
from gymkhana_listener import *


def gymkhana_main():

    json_config = open('tokens.json', 'r')
    tokens = json.load(json_config)
    json_config.close()

    consumer_key = tokens['consumer_key']
    consumer_secret = tokens['consumer_secret']
    access_token = tokens['access_token']
    access_token_secret = tokens['access_token_secret']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    listener = GymkhanaListener(api)
    stream = tweepy.Stream(api.auth, listener)
    filtro = ['@pytwe_bot', 'pytwe_bot', 'pytwe']
    stream.filter(track=filtro)

if __name__ == "__main__":
    gymkhana_main()