#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Stream listener of PyTweBot"""
import tweepy
from twitter_methods import MakingActions


 def __init__(self, api):
        super(PyTweListener, self).__init__()
        self.actions = MakingActions(api)

    def on_status(self, status):
        """Print a status text"""
        status.text = status.text.lower()
        if "ultra kek 0 name" in status.text:
            self.actions.retweet(status.id)
            self.actions.fav_tweet(status.id)
            print "@" + status.user.screen_name, status.created_at, status.text
        elif "y naci ciego" in status.text:
            self.actions.retweet(status.id)
            self.actions.fav_tweet(status.id)
            print "@" + status.user.screen_name, status.created_at, status.text
        elif "pytwe_bot" in status.text:
            if status.user.id != self.actions.get_api().me().id and not status.entities['user_mentions']:
                self.actions.quote_tweet("Dime", status)
            print "@" + status.user.screen_name, status.created_at, status.text
        elif "putos catalufos" in status.text:
            self.actions.quote_tweet("deja de dar tanto asco porfa \n", status)
            print "@" + status.user.screen_name, status.created_at, status.text
        elif status.text == 'nos vemo':
            self.actions.get_api().update_status("@" + status.user.screen_name + " en los bares", status.id)
            print "@" + status.user.screen_name, status.created_at, status.text
        elif status.text == 'whenpp te pasa':
            self.actions.get_api().update_status('@' + status.user.screen_name + " si xD", status.id)
            print "@" + status.user.screen_name, status.created_at, status.text

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

