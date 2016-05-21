#!/usr/bin/env bash

echo "Installing jasper modules"
read -p "Enter path to jasper home (/home/pi/Projects/jasper): " jasper_home
read -p "Enter path to plantbot home (/home/pi/Projects/plantbot3000): " plantbot_home

if [[ $jasper_home == "" ]]; then
  jasper_home="/home/pi/Projects/jasper"
fi

if [[ $plantbot_home == "" ]]; then
  plantbot_home="/home/pi/Projects/plantbot3000"
fi

echo $jasper_home
echo $plantbot_home

ln -s $plantbot_home/src/python/modules/plantbot.py $jasper_home/client/modules/plantbot.py
ln -s $plantbot_home/src/python/modules/hello.py $jasper_home/client/modules/hello.py
ln -s $plantbot_home/src/python/modules/hackathon.py $jasper_home/client/modules/hackathon.py
ln -s $plantbot_home/src/python/modules/beer.py $jasper_home/client/modules/beer.py

ln -s $plantbot_home/src/python/notifiers/plantbot_notify.py $jasper_home/client/plantbot_notify.py

echo ""
echo "Add the following lines to ~/.bashrc or ~/.bash_profile"
echo ""
printf "export PLANTBOT_HOME=%s\n" $plantbot_home

export PLANTBOT_HOME=$plantbot_home
