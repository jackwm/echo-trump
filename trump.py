#!/usr/bin/env python

import sys, os, twitter_oauth

def call_api(api):
    print [status.text for status in api.get_friends_timeline()]
    #friends = api.GetFriends()
    followers = api.GetFollowers()
    heathens = filter(lambda x: x not in followers,friends)
    print "There are %i people you follow who do not follow you:" % len(heathens)
    for heathen in heathens:
        print heathen.screen_name

def setup_client():
    consumer_key = os.getenv('TWITTER_KEY')
    consumer_secret = os.getenv('TWITTER_SECRET')
    oauth_token = os.getenv('OAUTH_TOKEN')
    oauth_token_secret = os.getenv('OAUTH_TOKEN_SECRET')
    api = twitter_oauth.Api(consumer_key, consumer_secret,oauth_token, oauth_token_secret)
    return api


if __name__ == "__main__":
    api = setup_client()
    call_api(api)
