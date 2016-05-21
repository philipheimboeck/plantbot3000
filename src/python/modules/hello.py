#!/usr/bin/env python
import re, sys, os

# Import required modules
sys.path.append(os.environ['PLANTBOT_HOME'] + "/src/python/")
from twitter import *

WORDS = ["HELLO", "WELCOME"]

def isValid(text):
    return bool(re.search(r'\bhello\b', text, re.IGNORECASE)) or  bool(re.search(r'\bwelcome\b', text, re.IGNORECASE))

def handle(text, mic, profile):

    message = "Hello Julian, it is nice to be here in Dornbirn today"
    tweet(message)

    mic.say(message)
