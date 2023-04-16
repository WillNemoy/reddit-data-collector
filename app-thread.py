import praw
from praw.models import MoreComments

from psaw import PushshiftAPI


import pandas as pd
import openpyxl

import os
from dotenv import load_dotenv
import json
import datetime
import time

load_dotenv() # look in the ".env" file for env vars

from textblob import TextBlob
import re

import pandas as pd
import numpy as np

def extract_keywords(text):

    # Using filter() and lambda function to filter out punctuation characters
    def remove_punctuation(text):
        result = ''.join(filter(lambda x: x.isalpha() or x.isdigit() or x.isspace(), str(text)))
        return result

    #remove punctutation
    text = remove_punctuation(text)

    #select noun phrases
    txtBlob = TextBlob(text).noun_phrases

    noun_phrases = []
    
    #only return noun phrases with at least 2 words
    for phrase in txtBlob:
            if (" " in phrase):
                noun_phrases.append(phrase)

    return noun_phrases

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

def redditAPIcomments(user_input, REDDIT_API_KEY_PARA, REDDIT_API_KEY_SECRET_PARA, USER_AGENT_PARA, file_name):

    reddit = praw.Reddit(client_id = REDDIT_API_KEY_PARA, #peronal use script
                        client_secret = REDDIT_API_KEY_SECRET_PARA, #secret token
                        user_agent = USER_AGENT_PARA)

    author_list = []
    text_list = []
    created_at_list = []
    score_list = []
    
    id_list = []
    is_submitter_list = []
    permalink_list = []
    stickied_list = []


    
    post = reddit.submission(url=user_input)
    post.comments.replace_more(limit=None)
    for top_level_comment in post.comments:
        print(top_level_comment.author)
        print(clean_text(top_level_comment.body))
        print(top_level_comment.created_utc)
        print(top_level_comment.score)

        print(top_level_comment.id)
        print(top_level_comment.is_submitter)
        print(top_level_comment.permalink)
        print(top_level_comment.stickied)
        
        print()

        author_list.append(top_level_comment.author)
        text_list.append(clean_text(top_level_comment.body))
        created_at_list.append(top_level_comment.created_utc)
        score_list.append(top_level_comment.score)
        
        id_list.append(top_level_comment.id)
        is_submitter_list.append(top_level_comment.is_submitter)
        permalink_list.append(top_level_comment.permalink)
        stickied_list.append(top_level_comment.stickied)
       

    
    # initialize data of lists.
    reddit_data = {"Author": author_list,
                   "Text": text_list,
                   "Created At": created_at_list,
                   "Upvotes": score_list,
                   "Id": id_list,
                   "Is Submitter": is_submitter_list,
                   "Permalink": permalink_list,
                   "Stickied": stickied_list}

    # Create DataFrame
    df = pd.DataFrame(reddit_data)

    #create keywords DataFrame
    keywords_list = []
    index_list = []
    index = 0
    for text in df["Text"]:
        #here I should also remove punctuation and extract key phrases
        keywords = extract_keywords(text)

        for keywords in keywords:
            keywords_list.append(keywords)
            index_list.append(index)

        index += 1

    keywords_data = {"Index": index_list,
                     "Keywords": keywords_list}

    df_keywords = pd.DataFrame(keywords_data)

    filename = file_name + " Thread Reddit Data.xlsx"

    with pd.ExcelWriter(filename) as writer:  
        df.to_excel(writer, sheet_name='Reddit Thread')
        df_keywords.to_excel(writer, sheet_name='Keywords')


    
    
REDDIT_API_KEY = os.getenv("REDDIT_API_KEY")
REDDIT_API_KEY_SECRET = os.getenv("REDDIT_API_KEY_SECRET")
USER_AGENT = "Will Collecting Reddit Data test" #os.getenv("USER_AGENT")



#redditAPIcomments("https://www.reddit.com/r/WeAreTheMusicMakers/comments/10gkbj1/have_you_ever_successfully_pitched_your_song_for/", REDDIT_API_KEY, REDDIT_API_KEY_SECRET, USER_AGENT)

josh_URLs = ["https://www.reddit.com/r/WeAreTheMusicMakers/comments/ezkjed/for_all_the_working_musicians_and_producers_out/",
            "https://www.reddit.com/r/WeAreTheMusicMakers/comments/ko8fox/a_music_label_wants_to_invest_in_my_music_and_i/",
            "https://www.reddit.com/r/WeAreTheMusicMakers/comments/bcegae/spotify_turns_over_about_5_billion_annually/",
            "https://www.reddit.com/r/WeAreTheMusicMakers/comments/9x2h76/i_work_in_music_marketing_and_i_always_struggle/",
            "https://www.reddit.com/r/WeAreTheMusicMakers/comments/jhgh6t/made_this_with_my_artist_data_to_show_the/",
            "https://www.reddit.com/r/shareyourmusic/comments/isnpj2/im_tired_of_huge_playlists_charging_money_for/",
            "https://www.reddit.com/r/musicians/comments/rbhl2q/just_a_warning_for_all_musicians/",
            "https://www.reddit.com/r/WeAreTheMusicMakers/comments/e6o4gu/we_protested_and_soundcloud_listened/"]

count = 1
for url in josh_URLs:
    try:
        redditAPIcomments(url, REDDIT_API_KEY, REDDIT_API_KEY_SECRET, USER_AGENT, str(count))
    except:
        nothing = "nothing"
        
    count += 1
    time.sleep(100)
