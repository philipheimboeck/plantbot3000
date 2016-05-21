#!/usr/bin/env python
import re, sys, os

# Import required modules
sys.path.append(os.environ['PLANTBOT_HOME'] + "/src/python/")
from sensor_reader import SensorReader

WORDS = ["HOW", "ARE", "YOU"]

reader = SensorReader()

def isValid(text):
    return bool(re.search(r'\bhow are you\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    reader.read()
    light = reader.getLightPercentage()
    moist = reader.getMoistPercentage()

    message = "My moist level is %d percentage and my light level is %d percentage" % (moist, light)

    mic.say(message)
