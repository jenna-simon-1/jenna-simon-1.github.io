from twitter import Twitter, OAuth

import tweepy
import pandas as pd
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_key = os.environ.get("api_key")
api_secret = os.environ.get("api_secret")
access_token = os.environ.get("access_token")
access_secret = os.environ.get("access_secret")

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
search = "#tfatws"

day1 = tweepy.Cursor(api.search,
              q=search,
              lang="en", since="2021-03-21",
                   until="2021-03-22").items(100)

day2 = tweepy.Cursor(api.search,
              q=search,
              lang="en", since="2021-03-22",
                   until="2021-03-23").items(100)

day3 = tweepy.Cursor(api.search,
              q=search,
              lang="en", since="2021-03-23",
                   until="2021-03-24").items(100)

day4 = tweepy.Cursor(api.search,
              q=search,
              lang="en", since="2021-03-24",
                   until="2021-03-25").items(100)

day5 = tweepy.Cursor(api.search,
              q=search,
              lang="en", since="2021-03-25",
                   until="2021-03-26").items(100)

day6 = tweepy.Cursor(api.search,
              q=search,
              lang="en", since="2021-03-26",
                   until="2021-03-27").items(100)

day7 = tweepy.Cursor(api.search,
              q=search,
              lang="en", since="2021-03-27",
                   until="2021-03-28").items(100)

days = [day1, day2, day3, day4, day5, day6, day7]
tweets = []

for day in days:
     data = [[tweet.user.screen_name, tweet.text, tweet.lang, tweet.created_at, tweet.favorite_count, tweet.retweet_count] for tweet in day]
     tweets.append(pd.DataFrame(data=data, 
                    columns=['user', 'text', 'lang', 'created_at', 'favorite_count', 'retweet_count']))

df = pd.concat(tweets)

df.reset_index(inplace=True)
del df['index']

df.to_csv('tfatws.csv')