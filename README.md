# PyTwe-Bot
A short twitter bot made with Python.

Currently the bot is hosted in a Raspberry Pi 3 model b with Ubuntu 16.04.3. 

Made with Tweepy 3.5.0 (http://tweepy.readthedocs.io/en/v3.5.0/index.html) and Python 2.7




Class PyTweListener: This method will stop the stream if you exceed the allowed the number of connections to the twitter API.
The BotListener is just a class that extends from tweepy.StreamListener. The method on_status is just the actions you'll do when there's a new tweet in the stream. The methon on_error just ends the stream if the stream raises the error 420.

```python
    def on_error(self, status_code):
        if status_code == 420:
            return False
```

In the class TwitterMethods you can find some algorithms that you can use with your authenticated twitter account.
The methods that are commented is because aren't working correctly and I'm trying to fix or replace that methods.

The script tweet_current_status.py is necessary tu run it in a Raspberry Pi. The script take some info from the current status of the Rpi and tweets it to the world.

The first command executes the program /opt/vc/bin/vcgencmd with the measure_temp argument, and the output it's saved in current_temp, same with current_mem. This is useful information of the RPi's status.
```python
    current_temp = subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
    current_mem = subprocess.check_output(["free", "-h"])
````

The special_actions.py is a class that makes special things with some python libraries. Currently just creates an image with a given text. If you want to use that class you'll need python-wand, that requieres imagemagick 6.


```sh
    sudo apt-get install python-wand
```

Ubuntu 16.04.3 has already installed imagemagick 6. 
