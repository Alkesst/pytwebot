#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made with python 2.7
# @Alkesstt at twitter. Alkesst @ telegram and GitHub.
import tweepy
from os import listdir
from os.path import isfile, join



class GymkanaCEUMA(object):

    def __init__(self, api, path):
        self.api = api
        self.path = path
        self.counter = 0

    def tweeting_images(self, user_id, status_id):
        self.api.update_with_media(self.path + self.from_file_to_list[self.counter],
                                   status=('@' + self.api.get_user(id=user_id).screen_name + ' Buena suerte!!'),
                                   in_reply_to_status_id=status_id)
        self.counter += 1

    def tweeting_felicitacion(self, user_id, status_id):
        self.api.update_status(status='@' + self.api.get_user(id=user_id).screen_name + 'Enhorabuena, lo has '
                                                                                        'encontrado!!',
                               in_reply_to_status_id=status_id)

    @property
    def from_file_to_list(self):
        only_files = [f for f in listdir(self.path) if isfile(join(self.path, f)) and f != '.DS_Store']
        return only_files
