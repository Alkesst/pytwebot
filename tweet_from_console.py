from __future__ import absolute_import, print_function

import tweepy

def main():
    """Just a main"""
    consumer_key = ""
    consumer_secret = ""


    access_token = ""
    access_token_secret = ""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)


    print(api.me().name)



    if raw_input("El twit contiene alguna imagen? ") == "no":
        tweet = raw_input("Que quieres tweetear? ")
        api.update_status(str(tweet))

    else:
        tweet = raw_input("Que quieres tweetear? ")
        file_name = raw_input("Que nombre tiene el archivo? ")
        api.update_with_media(file_name, tweet)

if __name__ == "__main__":
    main()
    