#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Stream listener of PyTweBot"""
import tweepy
from twitter_methods import MakingActions


class PyTweListener(tweepy.StreamListener):
    """Hey"""

    def __init__(self, api):
        super(PyTweListener, self).__init__()
        self.actions = MakingActions(api)

    def on_status(self, status):
        """Print a status text"""
        self.actions.fav_tweet(status.id)
        print "@" + status.user.screen_name, status.created_at, status.text
        status.text = status.text.lower()
        if "ultra kek 0 name" in status.text:
            self.actions.retweet(status.id)
        elif "y naci ciego" in status.text:
            self.actions.retweet(status.id)
        elif "pytwe_bot" in status.text:
            if status.user.id != self.actions.get_api().me().id and not status.entities['user_mentions']:
                self.actions.quote_tweet("Dime", status)
        elif "putos catalufos" in status.text:
            self.actions.quote_tweet("deja de dar tanto asco porfa \n", status)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
