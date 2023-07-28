#!/bin/bash


sudo apt-get update -y
sudo apt-get install aria2 -y
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/phoenix-1708/DR_NED/resolve/main/checkpoints.zip -d /workspaces/dn/checkpoints -o checkpoints.zip
unzip /workspaces/dn/checkpoints/checkpoints.zip
mv *.lib /workspaces/dn/checkpoints
cd preprocessing
python -m pip install --upgrade pip
pip install -r requirements.txt
sudo apt-get install ffmpeg libsm6 libxext6 -y
cd ..
python bot.py
