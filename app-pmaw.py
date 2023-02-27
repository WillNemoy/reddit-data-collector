from pmaw import PushshiftAPI

import pandas as pd

import datetime as dt

api = PushshiftAPI()

def reddit_pushshift_comments():
    before = int(dt.datetime(2021,2,1,0,0).timestamp())
    after = int(dt.datetime(2020,12,1,0,0).timestamp())

    subreddit="wallstreetbets"
    limit=100
    comments = api.search_comments(subreddit=subreddit, limit=limit, before=before, after=after)
    print(f'Retrieved {len(comments)} comments from Pushshift')

    comments_df = pd.DataFrame(comments)

    comments_df.to_excel("Test.xlsx")



reddit_pushshift_comments()