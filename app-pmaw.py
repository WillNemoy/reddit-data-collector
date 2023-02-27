from pmaw import PushshiftAPI
import pandas as pd
import datetime as dt

api = PushshiftAPI()

def reddit_pushshift_comments():

    comments = api.search_submission_comment_ids(ids=["11dhf1t"])
    print(f'Retrieved {len(comments)} comments from Pushshift')

    comments_df = pd.DataFrame(comments)

    comments_df.to_excel("Test.xlsx")



def reddit_pushshift_subreddit():


    after = int(dt.datetime(2023,1,1,0,0).timestamp())

    def fxn(item):
        return item['score'] > 2

    comments = api.search_submissions(q="cat", subreddit="MadeMeSmile", limit=100)
    print(f'Retrieved {len(comments)} submissions from Pushshift')

    comments_df = pd.DataFrame(comments)

    comments_df.to_excel("Test.xlsx")


reddit_pushshift_comments()