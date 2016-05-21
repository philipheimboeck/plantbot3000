#!/usr/bin/env python
import sys, os
import random, re

# Import required modules
sys.path.append(os.environ['PLANTBOT_HOME'] + "/src/python/")
from twitter import *

WORDS = ["HELLO", "WELCOME", "GREETINGS"]

def isValid(text):
    return bool(re.search(r'((\bhello|greetings|welcome\b))', text, re.IGNORECASE))

def handle(text, mic, profile):


    messages = ["Hello %s, it is nice to be in %s today." % (profile["first_name"], profile["location"]),
                "Greetings %s! You are allowed to spoil me today." % (profile['first_name']),
                "Hello %s. What is it what you want?" % (profile['first_name']),
                "I don't feel like talking right now.",
                "People were always talking to me. But at least I didn't had to answer."]

    message = random.choice(messages);

    tweet(message)

    mic.say(message)