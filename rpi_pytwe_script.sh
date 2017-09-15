#!/usr/bin/env bash
cd /home/pi/Documentos/PyTwe-Bot
echo "Pulling PyTwe-Bot..."
echo
git pull
echo
echo "Pull done..."
echo "Initializating PyTwe-Bot..."
echo nope | python stream_bot.py
