#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


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
hashtag = ['فوركس','تعلم كيف تجني ارباح','قصة نجاح','حقق ارباح','من موظف بسيط الى رجل اعمال','لحظة استلامه سيارته المايباخ']
print ('Running bot: @' + mybot.screen_name + '\nUsing list: ' + mylist.name + ' Members Count: ' + str(mylist.member_count) + 'Subs Count' + str(mylist.subscriber_count))

i = 0
while i < len(hashtag):
    for tweet in tweepy.Cursor(api.search,q=hashtag[i],lang='ar').items(5):
        try:
            if tweet.user.id == mybot.id:
                continue
            print ('\n\nFound a tweet by: @' + tweet.user.screen_name)
            if(tweet.retweeted == False) or (tweet.favorited == False):
                tweet.retweet()
                # tweet.favorite()
                print ('Retweeted and Favorited the tweet')
            m = "@%s not true" % (tweet.user.screen_name)
            api.update_status(status=m, in_reply_to_status_id=tweet.id)
            trends1 = api.trends_place(23424938)
            for trend in trends1[0]['trends']:
                print (trend['name'])

            if(tweet.user.following == False):
                # tweet.user.follow()
                print ('Followed the user')
            uopen = open('users.txt','a')
            uopen.write ( '@' + tweet.user.screen_name + ': ' + str(tweet.user.id)+'\n' + str(tweet.text) + '\n' + str(tweet.created_at) + '\n\n' + '\n\n')
            uopen2 = open('trends.txt', 'a')
            uopen2.write(trend['name'] + '\n')
            uopen.close()
            uopen2.close()
        except tweepy.TweepError as e:
            print (e.reason)
            sleep(10)
            continue
        except StopIteration:
            pass
    i +=1

