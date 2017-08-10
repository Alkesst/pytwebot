from __future__ import absolute_import, print_function

import tweepy

#Add your tokens from the devs.twitter web 
consumer_key = ""
consumer_secret = ""
#Access tokens are for making actions with your twitter account
access_token = ""
access_token_secret = ""

#authenticating your account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


print(api.me().name)

#A friendly way to ask what do you want to tweet in your account
tweet = raw_input("Que quieres tweetear?")
api.update_status(str(tweet))
