# PyTwe-Bot
A short twitter bot made with Python.
Made with Tweepy 3.5.0 (http://tweepy.readthedocs.io/en/v3.5.0/index.html) and Python 2.7


Class PyTweListener: This method will stop the stream if you exceed the allowed the number of connections to the twitter API
```python
    def on_error(self, status_code):
        if status_code == 420:
            return False
```

In the class TwitterMethods you can find some algorithms that you can use with your authenticated twitter account.
The methods that are commented is because aren't working correctly and I'm trying to fix or replace that methods.
