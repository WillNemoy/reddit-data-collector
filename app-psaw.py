from psaw import PushshiftAPI

# Initialize PushShift
api = PushshiftAPI()

gen = api.search_submissions(subreddit='MadeMeSmile', limit=1)
results = list(gen)

print(results)