#!/usr/bin/env bash
cd /home/pi/Documentos/PyTwe-Bot/tweeting_quijote
STATE=$(ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && echo ok || echo error)
while [  $STATE == "error" ]; do
    STATE=$(ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && echo ok || echo error)
    sleep 2
 done
echo "Initializating Quijote Script..."
echo
echo "Publishing Quijote..."
python main_quijote.py
