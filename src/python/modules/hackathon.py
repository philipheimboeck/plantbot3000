#!/usr/bin/env python
import re, sys, os

# Import required modules
sys.path.append(os.environ['PLANTBOT_HOME'] + "/src/python/")
from twitter import *

WORDS = ["umahuesla", "hackathon", "uma", "hysla"]

def isValid(text):
    return bool(re.search(r'\bhackathon\b', text, re.IGNORECASE)) or  bool(re.search(r'\buma\b', text, re.IGNORECASE))

def handle(text, mic, profile):

    message = "You know what " + profile["first_name"] + "? I REALLY LOVE NERDS AND GEEKS!"
    tweet(message)

    mic.say(message)
