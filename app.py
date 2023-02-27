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



def clean_text(x):
    
        new_text = ""

        for character in x:
            if (character.isalnum() == True 
                or character == " "
                or character == "'"
                or character == "#"
                or character == "-"
                or character == "("
                or character == ")"
                or character == "&"
                or character == "%"
                or character == "$"
                or character == "@"
                or character == "*"
                or character == ":"
                or character == ";"
                or character == "."
                or character == "?"
                or character == "/"
                or character == "["
                or character == "]"
                or character == "{"
                or character == "}"
                or character == "="
                or character == "!"
                or character == "<"
                or character == ">"
                or character == ","
                or character == ""
                or character == "_"
                or character == "+"):

                new_text += character

        return new_text

for submission in reddit.subreddit("MadeMeSmile").top(time_filter="all", limit=10):
    print(clean_text(submission.title))
    print(submission.author)
    print(submission.author_flair_text)
    print(submission.created_utc)
    print(submission.id)
    print(submission.num_comments)
    print(submission.permalink)
    print(submission.score)
    print(submission.upvote_ratio)
    print(submission.url)
    print()


# Output: 10 submissions