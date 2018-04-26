import os
import tweepy

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def fetch_tweets_for_account(screen_name, limit=50):
    """
    Fetch Tweets for account using screen_name
    :param screen_name: Screen name of account
    :param limit: Max tweets to be fetched
    :return: a list of tweet objects
    """
    tweets = api.user_timeline(id=screen_name, count=limit)
    return tweets
