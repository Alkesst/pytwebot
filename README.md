# PyTwe-Bot
A short twitter bot made with Python.
Made with Tweepy 3.5.0 (http://tweepy.readthedocs.io/en/v3.5.0/index.html) and Python 2.7


Class PyTweListener: This method makes the Stream stop if you exceed the limit number of attempts
```python
    def on_error(self, status_code):
        if status_code == 420:
            return False
```
