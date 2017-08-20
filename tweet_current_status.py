#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just a main"""
import subprocess
import time
import tweepy
import nltk


def main():
    """Hace cosas"""
    consumer_key = ""
    consumer_secret = ""

    access_token = ""
    access_token_secret = ""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    while True:
        current_temp = subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
        current_mem = subprocess.check_output(["free", "-h"])
        current_mem = current_mem.splitlines()
        tokenizer = nltk.tokenize.RegexpTokenizer(r'[M0-9]+')
        tokenized_text = tokenizer.tokenize(current_mem[1])
        cont = 0
        for items in tokenized_text:
            if cont == 2:
                used_mem = items
            elif cont == 3:
                free_mem = items
            cont += 1
        api.update_status("Current RPI 3 status: \n" + "Used Memory: " + str(used_mem) + "\nFree Memory: " + str(free_mem) + "\n" + str(current_temp) + "\n" + time.strftime("%H:%M:%S"))
        time.sleep(3600)
if __name__ == "__main__":
    main()
