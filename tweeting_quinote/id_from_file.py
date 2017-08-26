#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C1001
# pylint: disable=C0111
# pylint: disable=R0903


class GettingId():

    def __init__(self, file_name):
        self.file = file_name

    def get_id_from_file(self):
        file_id = open(self.file, 'r')
        return file_id.readline()

    def save_id_to_file(self, status_id):
        file_id = open(self.file, 'w')
        file_id.write(str(status_id)+ "\n")
