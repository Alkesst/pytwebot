#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C1001
"""a"""

class QuijoteTweet():
    """a"""

    def __init__(self, file_name_read, file_name_write):
        self.file_name_read = file_name_read
        self.file_name_write = file_name_write
        self.list = []

    def get_quijote_tweet(self):
        """make all the process"""
        txt_file = open(self.file_name_read, 'r')
        seekline = 0
        try:
            position_file = open(self.file_name_write, 'r')
            seekline = position_file.readline()
            txt_file.seek(int(seekline))
            position_file.close()
        except IOError:
            seekline = 0
        print seekline
        line = txt_file.read(139)
        position_file = open(self.file_name_write, 'w')
        pos = line.rfind(" ")
        position_file.write(str(int(seekline) + pos) + "\n")
        line = line[0:pos]
        position_file.close()
        txt_file.close()
        return line

    def file_lines(self):
        """a"""
        pass

    def callate(self):
        """a"""
        pass