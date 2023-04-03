import praw
from praw.models import MoreComments

from psaw import PushshiftAPI


import pandas as pd
import openpyxl

import os
from dotenv import load_dotenv
import json
import datetime

load_dotenv() # look in the ".env" file for env vars

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

def redditAPIsubbreddit(user_input, user_limit, REDDIT_API_KEY_PARA, REDDIT_API_KEY_SECRET_PARA, USER_AGENT_PARA):

    reddit = praw.Reddit(client_id = REDDIT_API_KEY_PARA, #peronal use script
                        client_secret = REDDIT_API_KEY_SECRET_PARA, #secret token
                        user_agent = USER_AGENT_PARA)

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

    for post in reddit.subreddit(user_input).hot(limit=user_limit):
    #for post in reddit.subreddit(user_input).top(time_filter="all", limit=1000):
        title_list.append(clean_text(post.title))
        author_list.append(post.author)
        created_time_list.append(post.created_utc)
        
        upvotes_list.append(post.score)
        comments_list.append(post.num_comments)
        upvote_ratio_list.append(post.upvote_ratio)

        id_list.append(post.id)
        name_list.append(post.name)

        permalink_list.append(post.permalink)
        url_list.append(post.url)
 


    
    # initialize data of lists.
    reddit_data = {"Title": title_list,
                   "Author": author_list,
                   "Date": created_time_list,
                   "Upvotes": upvotes_list,
                   "Comments": comments_list,
                   "Upvote Ratio": upvote_ratio_list,
                   "Id": id_list,
                   "Name": name_list,
                   "Permalink": permalink_list,
                   "URL": url_list}
                
    
    # Create DataFrame
    df = pd.DataFrame(reddit_data)

    keywords_list = []
    index_list = []
    index = 0
    for text in df["Text"]:
        #here I should also remove punctuation and extract key phrases
        keywords = text.split(" ")

        for keywords in keywords:
            keywords_list.append(keywords)
            index_list.append(index)

        index += 1


    
    filename = user_input + " Reddit Data.xlsx"
    
    
    with pd.ExcelWriter("web_app/" + file_name) as writer:  
        df.to_excel(writer, sheet_name='Data')
        df_sheet2.to_excel(writer, sheet_name='Abstract Words')
        df_sheet3.to_excel(writer, sheet_name='Headline Words')
        df_sheet4.to_excel(writer, sheet_name='Article Keywords')
    
REDDIT_API_KEY = os.getenv("REDDIT_API_KEY")
REDDIT_API_KEY_SECRET = os.getenv("REDDIT_API_KEY_SECRET")
USER_AGENT = "Will Collecting Reddit Data test" #os.getenv("USER_AGENT")


redditAPIsubbreddit("MadeMeSmile", 100, REDDIT_API_KEY, REDDIT_API_KEY_SECRET, USER_AGENT)




















def redditAPIcomments(user_input, REDDIT_API_KEY_PARA, REDDIT_API_KEY_SECRET_PARA, USER_AGENT_PARA):

    reddit = praw.Reddit(client_id = REDDIT_API_KEY_PARA, #peronal use script
                        client_secret = REDDIT_API_KEY_SECRET_PARA, #secret token
                        user_agent = USER_AGENT_PARA)

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

    
    post = reddit.submission(user_input)
    post.comments.replace_more(limit=None)
    for top_level_comment in post.comments:
        print(clean_text(top_level_comment.author))
        print(clean_text(top_level_comment.body))
        print(clean_text(top_level_comment.created_utc))
        print(clean_text(top_level_comment.id))
        print(clean_text(top_level_comment.is_submitter))
        print(clean_text(top_level_comment.permalink))
        print(clean_text(top_level_comment.stickied))
        print(clean_text(top_level_comment.score))

    
    # initialize data of lists.
    reddit_data = {"Title": title_list,
                   "Author": author_list,
                   "Date": created_time_list,
                   "Upvotes": upvotes_list,
                   "Comments": comments_list,
                   "Upvote Ratio": upvote_ratio_list,
                   "Id": id_list,
                   "Name": name_list,
                   "Permalink": permalink_list,
                   "URL": url_list}





def redditAPItest(user_input, REDDIT_API_KEY_PARA, REDDIT_API_KEY_SECRET_PARA, USER_AGENT_PARA):

    reddit = praw.Reddit(client_id = REDDIT_API_KEY_PARA, #peronal use script
                        client_secret = REDDIT_API_KEY_SECRET_PARA, #secret token
                        user_agent = USER_AGENT_PARA)
            

    fullnames = [user_input] 
    for i, submission in enumerate(reddit.info(fullnames=fullnames)):
        print(f"Processing post:{i}, with ID: {submission.id}")


    for post in reddit.subreddit(user_input).hot(limit=1000):
    #for post in reddit.subreddit(user_input).top(time_filter="all", limit=1000):
        print(post.author)


    #print(reddit.subreddit("MadeMeSmile").fullname)




                
    





"""
#https://psaw.readthedocs.io/en/latest/

import datetime as dt

reddit = praw.Reddit(client_id = REDDIT_API_KEY, #peronal use script
                    client_secret = REDDIT_API_KEY_SECRET, #secret token
                    user_agent = USER_AGENT)

api = PushshiftAPI(reddit)


start_epoch=int(dt.datetime(2017, 1, 1).timestamp())

my_list = list(api.search_submissions(after=start_epoch,
                            subreddit='politics',
                            filter=['url','author', 'title', 'subreddit'],
                            limit=10))

print(my_list)
"""


