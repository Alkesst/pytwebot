#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A twitter for console."""
import tweepy


class MakingActions:
    """Abstraction of making actions with twitter."""

    def __init__(self, api):
        self.api = api

    def new_tweet(self, tweet):
        """Creates a new tweet"""
        self.api.update_status(str(tweet))

    def retweet(self, tweet_id):
        """Retweet a tweet from id"""
        if not self.get_tweet(tweet_id).retweeted:
            self.api.retweet(tweet_id)

    def get_tweet(self, tweet_id):
        """Return a Status object from a tweet ID"""
        return self.api.get_status(tweet_id)

    def fav_tweet(self, tweet_id):
        """Favorites the tweet given"""
        if not self.get_tweet(tweet_id).favorited:
            self.api.create_favorite(tweet_id)

    def follow_account(self, user_id):
        """Follow an account_id"""
        self.api.create_friendship(user_id)

    def get_api(self):
        """Returns the API object"""
        return self.api
    
    def quote_tweet(self, text, status):
        """Quote a status"""
        self.api.update_status(str(text) + " twitter.com/" + str(status.user.screen_name) + "/status/" + str(status.id))


    #def get_following(self):
    #    """Return a list of the following followers"""
    #    following = []
    #    followers = self.get_followers(self.api.me().screen_name)
    #    for follower in followers:
    #        if not follower.following:
    #            following.append(follower)
    #    return following

    def get_user_from_tweet(self, tweet_id):
        """Returns an User object from a given tweet"""
        tweet = self.get_tweet(tweet_id)
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

    def get_tweets_from_timeline(self):
        """Returns a list of all the tweets from the home timeline"""
        tweets = []
        for status in tweepy.Cursor(self.api.home_timeline).items(200):
            tweets.append(status)
        return tweets

    @staticmethod
    def get_id_from_list(tweets_list):
        """Gets the id from a list of tweets and return a list of all id's from the tweets"""
        ids = []
        for tweets in tweets_list:
            ids.append(tweets.id)
        return ids


    def fav_from_list(self, list_id):
        """Fav every tweet in a list"""
        for items in list_id:
            self.fav_tweet(items)

    @staticmethod
    def get_text_from_list(tweets_list):
        """Returns the text of all tweets from a list"""
        text = []
        for tweets in tweets_list:
            text.append(tweets.text)
        return text

    #def folowback(self):
    #    """Follow all accounts that follows you and you don't follow them."""
    #    followers = self.get_followers(self.api.me().screen_name)
    #    following = self.get_following()
    #    for follower in followers:
    #        if follower not in following:
    #            self.follow_account(follower.id)

    def get_user_tweets(self):
        """Returns a list of all tweets from the authenticathed API user."""
        tweets = []
        for status in tweepy.Cursor(self.api.user_timeline).items():
            tweets.append(status)
        return tweets

    def get_interactions_from_tweets(self):
        """Print the number of favs and rt's """
        tweets = self.get_user_tweets()
        for items in tweets:
            print items.text 
            print str(items.favorite_count) + " Favs"
            print str(items.retweet.count) + " Retweets"

    def get_retweets(self, tweet_id=0):
        """Returns a list of the retweeted tweets from the authenticated api acc.
        If the argument tweet_id is not equal to 0, then the list will return the earlier tweets
        than the tweet from the id"""
        if tweet_id == 0:
            rts = self.api.retweets_of_me()
        else:
            rts = self.api.retweets_of_me(tweet_id)
        return rts

    def get_mentions_from_timeline(self):
        """Returns a list of all the tweets from the home timeline"""
        tweets = []
        for status in tweepy.Cursor(self.api.home_timeline, include_entities=True).items(200):
            if 'user_mentions' in status.entities:
                tweets.append(str(status.user.screen_name) + " " + str(status.created_at) + "\n" + status.text)
        mentions = []
        for items in tweets:
            if 'pytwe_bot' in items:
                mentions.append(items)
        return mentions
