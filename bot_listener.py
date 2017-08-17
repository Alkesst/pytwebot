#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Stream listener of PyTweBot"""
import tweepy

class PyTweListener(tweepy.StreamListener):
    """Hey"""
    def on_status(self, status):
        """Print a status text"""
        print status.text

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
