#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0301
# pylint: disable=R0912
# pylint: disable=E0012
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
        elif "y naci ciego" in text:
            self.actions.retweet(status.id)
            self.actions.fav_tweet(status.id)
        elif ("pytwe_bot" in text or "pytwe" in text) and text[0:2] != "RT":
            if status.user.id != self.actions.get_api().me().id and not status.entities['user_mentions']:
                self.actions.quote_tweet("Dime", status)
            self.actions.fav_tweet(status.id)
        elif "putos catalufos" in text and not text[0:2] != "RT":
            self.actions.quote_tweet("deja de dar tanto asco porfa \n", status)
            self.actions.fav_tweet(status.id)
        elif text[0:7] == 'nosvemo':
            self.actions.get_api().update_status("@" + status.user.screen_name + " en los bares", status.id)
            self.actions.fav_tweet(status.id)
            self.actions.retweet(status.id)
        elif text[0:12] == 'when te pasa':
            self.actions.get_api().update_status('@' + status.user.screen_name + " si xD", status.id)
            self.actions.fav_tweet(status.id)
            self.actions.retweet(status.id)
        elif text[0:10] == "mira macho":
            self.actions.get_api().update_status('@' + status.user.screen_name + " que te pasa fiera", status.id)
            self.actions.fav_tweet(status.id)
            self.actions.retweet(status.id)
        elif 'i like botijos' in text:
            self.actions.fav_tweet(status.id)
            self.actions.retweet(status.id)
        if text[0:15] == '@pytwe_bot ping':
            self.actions.fav_tweet(status.id)
            self.actions.get_api().update_status(status=("@" + status.user.screen_name + " Pong!"), in_reply_to_status_id=status.id)
        elif text[0:15] == '@pytwe_bot help':
            self.actions.fav_tweet(status.id)
            help_text = "@pytwe_bot search: te manda un meme personalizado con el texto que le añadas tras el search.\n"
            help_text += "@pytwe_bot ping: te responde con un pong. Sirve para saber si el bot está en funcionamiento.\n\n"
            help_text += "Interacciona con: when te pasa, nosvemo, putos catalufos, pytwe_bot, y naci ciego, ultra kek 0 name\n"
            self.actions.get_api().send_direct_message(screen_name=status.user.screen_name, text=help_text)
        elif "hora botijo" in text:
            self.actions.fav_tweet(status.id)
            self.actions.retweet(status.id)

        if text[0:17] == "@pytwe_bot search":
            to_image = text.encode('utf-8')
            try:
                SpecialActions.create_image_search("meme_template_search.png", to_image[18:len(to_image)])
                self.actions.get_api().update_with_media("generated_meme_search.png", "@" + status.user.screen_name + " ", in_reply_to_status_id=status.id)
                os.remove("generated_meme_search.png")
            except UnicodeEncodeError:
                self.actions.get_api().update_status("@" + status.user.screen_name + " evita poner caracteres raros como la cedilla o acentos porfa :)", status.id)
        if text[0:19] == "@pytwe_bot cabezas":
            try:
                pass
            except UnicodeEncodeError:
                pass

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False
