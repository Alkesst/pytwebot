#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made with python 2.7
# @Alkesstt at twitter. Alkesst @ telegram and GitHub.
from gymkhana_ceuma import *


class GymkhanaListener(tweepy.StreamListener):
    def __init__(self, api):
        super(GymkhanaListener, self).__init__()
        self.ceuma = GymkanaCEUMA(api, '/home/genericUsername/CEUMA/')

    def on_status(self, status):
        if status[0:31] == u'@pytwe_bot gymkhana informatica':
            self.ceuma.tweeting_images(status.user.id, status.id)
        if status[0:22] == u'@pytwe_bot encontrado!':
            self.ceuma.tweeting_felicitacion(status.user.id, status.status.id)

    def on_error(self, status_code):
        generic_var = True
        if status_code == 420:
            generic_var = False
        return generic_var
