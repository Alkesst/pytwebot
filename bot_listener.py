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

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
