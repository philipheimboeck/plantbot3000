#!/usr/bin/python
import sys, os

# Import required modules
sys.path.append(os.environ['PLANTBOT_HOME'] + "/TwitterAPI")
from TwitterAPI import TwitterAPI
from config import *

api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

def tweet(message):
    r = api.request('statuses/update', {'status': message})
    print('SUCCESS' if r.status_code == 200 else 'FAILURE ' + str(r.status_code) )
