import tweepy
import configparser
import pandas as pd

#Read the configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#Authentication to twitter api
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Get user tweets from nasdaq hashtag
keywords = '#QQQ'
limit = 1000

tweets = tweepy.Cursor(api.search_tweets, q = keywords, count = 100, tweet_mode = 'extended').items(limit)

#Create the dataframe for the tweets
columns = ['Time','User','Tweet']
data = []

for tweet in tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

#Export dataframe
df.to_csv('nasdaq_tweets.csv')