#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
apt-get update -y && apt-get install screen python python3 python3-pip -y
pip install -r requirements.txt && crontab -u $username crontab
