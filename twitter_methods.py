#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        """Favorites the twit given"""
        self.api.favorites(twit_id)

    def follow_account(self, user_id):
        """Follow an account_id"""
        self.api.create_friendship(user_id)

    def follow_all_followers(self, account_name):
        """Follow all the followers from a list"""
        ids = self.get_followers_id(account_name)
        for friends in ids:
            self.follow_account(friends)

    def get_followers_id(self, account_name):
        """Returns a list of all the followers of an account"""
        ids = []
        for page in tweepy.Cursor(self.api.followers_ids, screen_name=str(account_name)).pages():
            ids.extend(page)
        return ids

    #def get_following(self, account_name):
    #    """Return a list with all the following accounts"""
    #   ids = []
    #    for page in tweepy.Cursor(self.api.friends, screen_name=str(account_name)).pages():
    #       ids.extend(page)
    #  return ids

    def get_tweets_from_timeline(self):
        """Returns a list of all the tweets from the home timeline"""
        tweets = []
        for tweets in tweepy.Cursor(self.api.home_timeline).items(200):
            tweets.extend(tweets)
        return tweets

    @staticmethod
    def get_id_from_list(tweets_list):
        """Gets the id from a list of twits and return a list of all id's from the tweets"""
        ids = []
        for tweets in tweets_list:
            ids.append(tweets.id)
        return ids


    def fav_from_list(self, list_id):
        """Fav every twit in a list"""
        for items in list_id:
            self.fav_twit(items)

    @staticmethod
    def get_text_from_list(tweets_list):
        """Returns the text of all tweets from a list"""
        text = []
        for tweets in tweets_list:
            text.append(tweets.text)
        return text