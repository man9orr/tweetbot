#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from time import sleep


consumer_key = 'aKKl6MqQ5PEnrDHPEZqYAnEea'
consumer_secret = 'SvTNxs4lNljpsC3szqsT7FwhWBaWclNxOpTLRdDRaMbosXz6vG'
access_token = '852050791473057792-93yZUBEByxAjj6qfsLj7mTIWooOcrQN'
access_token_secret = 'fz8gft33iZTBRjGSGIOy7tuKzYUx6vJ0QB4h9outZHetW'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
auth.secure = True
api = tweepy.API(auth)
mybot = api.get_user(screen_name = '@anti_forex')
mylist = api.get_list('@' + mybot.screen_name,slug='sorry-for-adding-you')

print ('Running bot: @' + mybot.screen_name + '\nUsing list: ' + mylist.name + ' Members Count: ' + str(mylist.member_count) + 'Subs Count' + str(mylist.subscriber_count))
for tweet in tweepy.Cursor(api.search,q='#سوريا',lang='ar').items(5):
    try:
        if tweet.user.id == mybot.id:
            continue
        print ('\n\nFound a tweet by: @' + tweet.user.screen_name)
        if(tweet.retweeted == False) or (tweet.favorited == False):
            # tweet.retweet()
            # tweet.favorite()
            print ('Retweeted and Favorited the tweet')
        if(tweet.user.following == False):
            # tweet.user.follow()
            print ('Followed the user')
        uopen = open('users.txt','a')
        uopen.write ( '@' + tweet.user.screen_name + ': ' + str(tweet.user.id)+'\n' )
        uopen.close()
    except tweepy.TweepError as e:
        print (e.reason)
        sleep(10)
        continue
    except StopIteration:
        break

