#!/usr/bin/env python
import re, sys, os

# Import required modules
sys.path.append(os.environ['PLANTBOT_HOME'] + "/src/python/")
from twitter import *

WORDS = ["bier", "beer", "mohren", "pfiff"]

def isValid(text):
    return bool(re.search(r'\bbeer\b', text, re.IGNORECASE))

def handle(text, mic, profile):

    message = "No! I am just a plant and not your waitress!"

    mic.say(message)
