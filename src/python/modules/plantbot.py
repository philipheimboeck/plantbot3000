#!/usr/bin/env python
import re, sys, os, random

# Import required modules
sys.path.append(os.environ['PLANTBOT_HOME'] + "/src/python/")
from sensor_reader import SensorReader
from twitter import *

WORDS = ["HOW", "ARE", "YOU", "DO", "FEEL", "OK"]

reader = SensorReader()


def isValid(text):
    return bool(re.search(r'\b(how (are you)|(do you feel))|(you ok)\b', text, re.IGNORECASE))


def handle(text, mic, profile):
    reader.read()
    light = reader.getLightValue()
    moist = reader.getMoistPercentage()

    # message = "My moist level is %d percentage and my light level is %d percentage" % (moist, light)

    messages = ["You have a green thumb. I feel good.", "I feel fine.", "Today is a good day.",
                "Thank you for keeping me healthy.", "I am growing prosper. Thank you."]

    if moist < 40:
        messages = ["I am quite thirsty.", "Either give me water or kill me right now!",
                    "You must be confusing me with a cactus.", "Please net me right now!"]
    elif moist < 60:
        messages = ["I would like some water.", "It is not urgent, but could you net me?",
                    "Please net me."]

    if(light == 0):
        messages.append("I like the light in here.")
    else:
        messages.append("It is quite dark here.")

    message = random.choice(messages)

    tweet(message)
    mic.say(message)
