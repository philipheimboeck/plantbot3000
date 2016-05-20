#!/usr/bin/env python

from sensor_reader import SensorReader

WORDS = ["HOW", "ARE", "YOU"]

reader = SensorReader()

def isValid(text):
    return bool(re.search(r'\bhow are you\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    reader.read()
    light = reader.getLightValue()
    moist = reader.getMoistValue()

    moistState = "dry"
    if (light > 1024/2):
        moistState = "wet"

    message = "I am " + moistState

    mic.say(message)
