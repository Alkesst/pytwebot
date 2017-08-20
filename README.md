# PyTwe-Bot
A short twitter bot made with Python.

Currently the bot is hosted in a Raspberry Pi 3 model b. 

Made with Tweepy 3.5.0 (http://tweepy.readthedocs.io/en/v3.5.0/index.html) and Python 2.7


Class PyTweListener: This method will stop the stream if you exceed the allowed the number of connections to the twitter API
```python
    def on_error(self, status_code):
        if status_code == 420:
            return False
```

In the class TwitterMethods you can find some algorithms that you can use with your authenticated twitter account.
The methods that are commented is because aren't working correctly and I'm trying to fix or replace that methods.


These part of the BotListener.py is just for tracking some fragments of text from tweets you want to rt or fav
```python
        if "ultra kek 0 name" in status.text:
            self.actions.retweet(status.id)
        elif "y naci ciego" in status.text:
            self.actions.retweet(status.id)
        elif "pytwe_bot" in status.text:
            self.actions.retweet(status.id)
        elif "pickle rick" in status.text:
            self.actions.retweet(status.id)
        elif "pytwe_bot" in status.text:
            self.actions.quote_tweet("Dime", status)
```
The BotListener is just a class that extends from tweepy.StreamListener. The method on_status is just the actions you'll do when there's a new tweet in the stream. The methon on_error just ends the stream if the stream raises the error 420.

