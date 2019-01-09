from twython import Twython
import json
import pandas as pd


def get_query(query_term):
    with open('twitter_credentials.json', 'r') as file:
        credentials = json.load(file)

    tweets = Twython(credentials['CONSUMER_KEY'],
                     credentials['CONSUMER_SECRET'])

    query = {'q': query_term,
             'result_type': 'popular',
             'count': 100,
             'lang': 'en',
             }

    return tweets.search(**query)


def tweets_to_dict(tweets):
    tweets_dict = {'user': [], 'text': []}
    for status in tweets['statuses']:
        tweets_dict['user'].append(status['user']['name'])
        tweets_dict['text'].append(status['text'])
    return tweets_dict
