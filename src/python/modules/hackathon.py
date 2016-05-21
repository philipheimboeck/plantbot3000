#!/usr/bin/env python
import re, sys, os, random

# Import required modules
sys.path.append(os.environ['PLANTBOT_HOME'] + "/src/python/")
from twitter import *

WORDS = ["WHAT", "DO", "YOU", "THINK", "ABOUT", "CODING", "HACKING", "THE", "DEVELOPERS", "DEVELOPING", "HACKATHON"]

def isValid(text):
    return bool(re.search(r'\b(What do you think about )?coding|hacking|(the hackathon)|developers|developing\b', text, re.IGNORECASE)) or  bool(re.search(r'\buma\b', text, re.IGNORECASE))

def handle(text, mic, profile):

    messages = ["You know what %s? I really love nerds and geeks!" % (profile['first_name']),
                "It is very cool.",
                "I am only alive because of them",
                "Sometimes I wish I could code as well",
                ]

    message = random.choice(messages)
    tweet(message)

    mic.say(message)
