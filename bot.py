#!/usr/bin/env python
# -*- coding: utf-8 -*-
# made with python 2.7
"""A twitter for console."""
import tweepy


class MakingActions:
    """Abstraction of making actions with twitter."""

    def __init__(self, user, api):
        self.user = user
        self.api = api
    
    def new_twit(self, twit):
        """Creates a new twit"""
        self.api.update_status(str(twit))

    def fav_twit(self, twit_id):
        self.api.favorites(twit_id)
    
    def follow_all_followers(self, account_name):
        """Follow all the followers from an account"""
        ids = self.get_followers_id(account_name)
        #sigue a todos los users de una lista.
        for friends in ids:
            self.api.create_friendship(friends)
    
    def get_followers_id(self, account_name):
        """Returns a list of all the followers of an account"""
        ids = []
        for page in tweepy.Cursor(self.api.followers_ids, screen_name=str(account_name)).pages():
            ids.extend(page)
        return ids

    def get_following(self, account_name):
        ids = []
        for page in tweepy.Cursor(self.api.friends, screen_name=str(account_name)).pages():
            ids.extend(page)
        return ids

