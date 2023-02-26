import praw

import pandas as pd
import openpyxl

import os
from dotenv import load_dotenv
import json
import datetime



load_dotenv() # look in the ".env" file for env vars

REDDIT_API_KEY = os.getenv("REDDIT_API_KEY")
REDDIT_API_KEY_SECRET = os.getenv("REDDIT_API_KEY_SECRET")
USER_AGENT = os.getenv("USER_AGENT")



reddit = praw.Reddit(client_id = REDDIT_API_KEY, #peronal use script
                    client_secret = REDDIT_API_KEY_SECRET, #secret token
                    user_agent = USER_AGENT)

for submission in reddit.subreddit("MadeMeSmile").hot(limit=10):
    print(submission.title)

# Output: 10 submissions