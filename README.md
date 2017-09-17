# PyTwe-Bot
A short twitter bot made with Python.
## INTRODUCTION:

Currently the bot is hosted in a Raspberry Pi 3 model b with Ubuntu 16.04.3.

Made with Tweepy 3.5.0 (http://tweepy.readthedocs.io/en/v3.5.0/index.html) and Python 2.7




Class PyTweListener: This method will stop the stream if you exceed the allowed number of connections to the twitter API.
The BotListener is just a class that extends from tweepy.StreamListener. The method on_status is just the actions you'll do when there's a new tweet in the stream. The methon on_error just ends the stream if the stream raises the error 420.

```python
    def on_error(self, status_code):
        if status_code == 420:
            return False
```

In the class TwitterMethods you can find some algorithms that you can use with your authenticated twitter account.

The script tweet_current_status.py is necessary to be run it in a Raspberry Pi. The script take some info from the current status of the Rpi and tweets it to the world.

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

## AUTOMATE THE BOT

### Script

For initializing the bot when the rpi powers on you can use a service that executes a bash script like this:
```sh
    cd /home/user_name/PyTwe-Bot
    STATE=$(ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && echo ok || echo error)
    while [  $STATE == "error" ]; do
        #do a ping and check that its not a default message or change to grep for something else
        STATE=$(ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && echo ok || echo error)

        #sleep for 2 seconds and try again
        sleep 2
     done
    echo "Pulling PyTwe-Bot..."
    echo
    git pull
    echo
    echo "Pull done..."
    echo "Initializating PyTwe-Bot..."
    echo nope | python stream_bot.py
```

This check if there's internet connection, if not, wait 2 secs and retry a ping. I made this because, when the service
powers on, executes the script and raises an error from the python code informing that there's no internet connection.
```sh
STATE=$(ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && echo ok || echo error)
while [  $STATE == "error" ]; do
    #do a ping and check that its not a default message or change to grep for something else
    STATE=$(ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && echo ok || echo error)

    #sleep for 2 seconds and try again
    sleep 2
 done
```

When the script is executed it checks if there was any change in the code, and starts up the bot with the new changes.

### Service:
Now is needed to make the pytwe.service file:
```
[Unit]
Description=PyTwe-Bot

[Service]
ExecStart=/home/pi/rpi_pytwe_script.sh

[Install]
WantedBy=multi-user.target
```

Then, is requiered to put this file into /etc/systemd/system/. The user is not allowed to move files into /etc/systemd/system. It's necessary to use this command:
```sh
    sudo mv pytwe.service /etc/systemd/system
```

With this you enable the service, and will execute when the rpi powers on:
```sh
    sudo systemctl enable pytwe.service
```

Don't forget this:
```sh
    chmod a+x rpi_pytwe_script.sh
```

And now the script rpi_pytwe_script.sh will run always that the rpi powers on.
