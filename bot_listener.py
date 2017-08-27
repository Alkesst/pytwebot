#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0301
"""Stream listener of PyTweBot"""
import os
import tweepy
from special_actions import SpecialActions
from twitter_methods import MakingActions

class PyTweListener(tweepy.StreamListener):
    def __init__(self, api):
        super(PyTweListener, self).__init__()
        self.actions = MakingActions(api)

    def on_status(self, status):
        """Print a status text"""
        text = status.text.lower()
        if "ultra kek 0 name" in text:
            self.actions.retweet(status.id)
            self.actions.fav_tweet(status.id)
            print "@" + status.user.screen_name, status.created_at, status.text
        elif "y naci ciego" in text:
            self.actions.retweet(status.id)
            self.actions.fav_tweet(status.id)
            print "@" + status.user.screen_name, status.created_at, status.text
        elif "pytwe_bot" in text and text[0:2] != "RT":
            if status.user.id != self.actions.get_api().me().id and not status.entities['user_mentions']:
                self.actions.quote_tweet("Dime", status)
            print "@" + status.user.screen_name, status.created_at, status.text
            self.actions.fav_tweet(status.id)
        elif "putos catalufos" in text and not text[0:2] != "RT":
            self.actions.quote_tweet("deja de dar tanto asco porfa \n", status)
            print "@" + status.user.screen_name, status.created_at, status.text
            self.actions.fav_tweet(status.id)
        elif text[0:7] == 'nosvemo':
            self.actions.get_api().update_status("@" + status.user.screen_name + " en los bares", status.id)
            print "@" + status.user.screen_name, status.created_at, status.text
            self.actions.fav_tweet(status.id)
            self.actions.retweet(status.id)
        elif text[0:12] == 'when te pasa':
            self.actions.get_api().update_status('@' + status.user.screen_name + " si xD", status.id)
            print "@" + status.user.screen_name, status.created_at, status.text
            self.actions.fav_tweet(status.id)
            self.actions.retweet(status.id)
        elif text[0:10] == "mira macho":
            self.actions.get_api().update_status('@' + status.user.screen_name + " que te pasa fiera", status.id)
            print "@" + status.user.screen_name, status.created_at, status.text
            self.actions.fav_tweet(status.id)
            self.actions.retweet(status.id)

        if text[0:16] == "@pytwe_bot search":
            SpecialActions.create_image_search("meme_template_search.png", text[16:len(text)])
            self.actions.get_api().update_with_media("generated_meme_search.png", "@" + status.user.screen_name + " ", in_reply_to_status_id=status.id)
            os.remove("generated_meme_search.png")

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
