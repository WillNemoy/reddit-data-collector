import praw

import pandas as pd
import openpyxl

import os
from dotenv import load_dotenv
import json
import datetime

load_dotenv() # look in the ".env" file for env vars



def redditAPI(subbreddit_or_thread, user_input, REDDIT_API_KEY_PARA, REDDIT_API_KEY_SECRET_PARA, USER_AGENT_PARA)
    reddit = praw.Reddit(client_id = REDDIT_API_KEY_PARA, #peronal use script
                        client_secret = REDDIT_API_KEY_SECRET_PARA, #secret token
                        user_agent = USER_AGENT_PARA)


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

    title_list = []
    author_list = []
    created_time_list = []

    upvotes_list = []
    comments_list = []
    upvote_ratio_list = []

    id_list = []
    name_list = []

    permalink_list = []
    url_list = []

    for submission in reddit.subreddit(user_input).top(time_filter="all", limit=10):
        title_list.append(clean_text(submission.title))
        author_list.append(submission.author)
        created_time_list.append(submission.created_utc)
        
        upvotes_list.append(submission.score)
        comments_list.append(submission.num_comments)
        upvote_ratio_list.append(submission.upvote_ratio)

        id_list.append(submission.id)
        name_list.append(submission.name)

        permalink_list.append(submission.permalink)
        url_list.append(submission.url)


    
    # initialize data of lists.
    reddit_data = {"Title": title_list,
                "Author": author_list,
                "Date": created_time_list,
                "Upvotes": upvotes_list
                "Comments": comments_list,
                "Upvote Ratio": upvote_ratio_list,
                "Id": id_list,
                "Name": name_list,
                "Permalink": permalink_list,
                "URL": url_list}
    
    # Create DataFrame
    df = pd.DataFrame(data)

    filename = user_input + " Reddit Data.xlsx"
    
    df.to_excel(filename)

REDDIT_API_KEY = os.getenv("REDDIT_API_KEY")
REDDIT_API_KEY_SECRET = os.getenv("REDDIT_API_KEY_SECRET")
USER_AGENT = os.getenv("USER_AGENT")


redditAPI("subreddit", "MadeMeSmile", REDDIT_API_KEY, REDDIT_API_KEY_SECRET, USER_AGENT)