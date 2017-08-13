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

    def retweet(self, twit_id):
        """Retweet a tweet from id"""
        self.api.retweet(twit_id)

    def get_tweet(self, twit_id):
        """Return a Status object from a twit ID"""
        return self.api.get_status(twit_id)

    def fav_twit(self, twit_id):
        """Favorites the twit given"""
        self.api.create_favorite(twit_id)

    def follow_account(self, user_id):
        """Follow an account_id"""
        self.api.create_friendship(user_id)

    def get_following(self):
        """Return a list of the following followers"""
        following = []
        followers = self.get_followers(self.api.me.screen_name)
        for follower in followers:
            if not follower.following:
                following.append(follower)
        return following

    def get_user_from_twit(self, twit_id):
        """Returns an User object from a given tweet"""
        tweet = self.get_tweet(twit_id)
        return tweet.user

    def print_timeline(self):
        """A method that prints all the tweets from home_timeline"""
        tweets = self.get_tweets_from_timeline
        tweets = MakingActions.get_text_from_list(tweets)
        for items in tweets:
            print items

    def follow_all_followers(self, account_name):
        """Follow all the followers from a list"""
        ids = self.get_followers(account_name)
        for friends in ids:
            self.follow_account(friends)

    def get_followers(self, account_name):
        """Returns a list of all the followers of an account"""
        followers = []
        for page in tweepy.Cursor(self.api.followers_ids, screen_name=str(account_name)).pages():
            followers.extend(page)
        return followers

    #def get_following(self, account_name):
    #    """Return a list with all the following accounts"""
    #   ids = []
    #    for page in tweepy.Cursor(self.api.friends, screen_name=str(account_name)).pages():
    #       ids.extend(page)
    #  return ids

    def get_tweets_from_timeline(self):
        """Returns a list of all the tweets from the home timeline"""
        tweets = []
        for status in tweepy.Cursor(self.api.home_timeline).items(200):
            tweets.append(status)
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

    def folowback(self):
        """Follow all accounts that follows you and you don't follow them."""
        followers = self.get_followers(self.api.me.screen_name)
        following = self.get_following()
        for follower in followers:
            if follower not in following:
                self.follow_account(follower.id)

    def get_user_twits(self):
        """Returns a list of all tweets from the authenticathed API user."""
        tweets = []
        for status in tweepy.Cursor(self.api.user_timeline).items():
            tweets.append(status)
        return tweets

    def get_interactions_from_twits(self):
        """Print the number of favs and rt's """
        tweets = self.get_user_twits()
        for items in tweets:
            print items.text 
            print str(items.favorite_count) + " Favs"
            print str(items.retweet.count) + " Retweets"
