#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from time import sleep
import os
import sys
import random

reload(sys)
sys.setdefaultencoding('utf-8')

consumer_key = 'aKKl6MqQ5PEnrDHPEZqYAnEea'
consumer_secret = 'SvTNxs4lNljpsC3szqsT7FwhWBaWclNxOpTLRdDRaMbosXz6vG'
access_token = '852050791473057792-93yZUBEByxAjj6qfsLj7mTIWooOcrQN'
access_token_secret = 'fz8gft33iZTBRjGSGIOy7tuKzYUx6vJ0QB4h9outZHetW'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth)

for status in tweepy.Cursor(api.user_timeline).items():
    try:
        api.destroy_status(status.id)
        print "Deleted:", status.id
    except:
        print "Failed to delete:", status.id
