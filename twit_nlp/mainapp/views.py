from django.shortcuts import render
from twython import Twython  
import json

with open('twitter_credentials.json', 'r') as file:
    credentials = json.load(file)

def list_tweets(request):
    pass


