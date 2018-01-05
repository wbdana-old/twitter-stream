#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tweepy, json, time, sys, os

print(sys.argv[1])
if not sys.argv[1]:
    print("Need a hashtag to work with here buddy!")
    sys.exit()

HASHTAG = sys.argv[1]

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])
api = tweepy.API(auth)

class HashTagListener(tweepy.StreamListener):

    def on_status(self, status):
        print("tweet")
        print(status.text)

    def on_data(self, data):
        parsed = json.loads(data)
        print(parsed['text'])

    def on_error(self, status_code):
        print("error", str(status_code))
        if status_code == 420:
            return False

    def on_disconnect(self):
        print("DISCONNECT")
        return False

hashtag_listener = HashTagListener()
hashtag_stream = tweepy.Stream(auth = api.auth, listener = hashtag_listener, timeout=60)

hashtag_stream.filter(track = [str(HASHTAG)])