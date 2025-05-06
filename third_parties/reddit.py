import os
import praw
from dotenv import load_dotenv

def get_top_post_title(subreddit_name):
    load_dotenv()
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

    subreddit = reddit.subreddit(subreddit_name)
    top_post = next(subreddit.new(limit=1), None)

    return top_post.title if top_post else None
