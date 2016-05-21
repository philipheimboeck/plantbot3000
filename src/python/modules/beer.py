#!/usr/bin/env python
import re, sys, os, random

# Import required modules
sys.path.append(os.environ['PLANTBOT_HOME'] + "/src/python/")
from twitter import *

WORDS = ["PLEASE", "BRING", "BEER", "ME", "A", "PFIFF", "MOHREN", "FOHREN", "GIVE", "DRINK"]

def isValid(text):
    return bool(re.search(r'\b((please )?(bring|give) me a )?(beer|mohren|fohren|drink)\b', text, re.IGNORECASE))

def handle(text, mic, profile):

    messages = ["No! I am just a plant and not your waitress!",
                "You are kidding right? How would I do that?",
                "As soon as I grow some legs I will bring you one",
                "Today? Again?",
                "I think you might got a drinking problem"]

    message = random.choice(messages)

    mic.say(message)
