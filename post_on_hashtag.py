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
mybot = api.get_user(screen_name='@anti_forex')
mylist = api.get_list('@' + mybot.screen_name, slug='sorry-for-adding-you')
num_lines = sum(1 for line in open('trends.txt'))
second = 0
try:
    while (second <= num_lines):
        first = random.randint(0, 43)
        second = first + 3
        f = open('trends.txt').readlines()[first:second]
        r = open('temp.txt', 'w')
        r.writelines(f)
        r.close()
        hashHandle = open('temp.txt', 'r')
        temphash = hashHandle.read()
        hashHandle.close()
        print temphash
        message = 'احذروا من اعلانات الفوركس المشبوهه \n كلها كذب وتستهدف الخليج '
        message2 = 'احذروا من اعلانات الفوركس المشبوهه \n كلها خداع وتستهدف الخليج '
        message3 = 'انتبهوا من اعلانات الفوركس المشبوهه \n كلها كذب وتستهدف الخليج '
        message4 = 'ابعدوا من اعلانات الفوركس المشبوهه \n كلها جدل وتستهدف الخليج '
        message5 = 'احذروا من دعايات الفوركس المشبوهه \n كلها كذب وتستهدف الخليج '
        message6 = 'احذروا من حسابات الفوركس المشبوهه \n كلها كذب وتستهدف الخليج '
        message7 = 'احذروا دعايات الفوركس المشبوهه \n كلها كذب وتستهدف الخليج '
        message8 = 'احذروا اعلانات الفوركس المشبوهه \n كلها كذب وتستهدف الخليج '
        message9 = 'ابتعدوا من دعايات الفوركس المشبوهه \n كلها كذب وسرقة امول '
        message10 = 'احذروا من دعايات الفوركس المشبوهه \n كلها سرقة وخداع '
        message11 = 'احذروا من دعايات الفوركس المشبوهه \n كلها نصب واحتيال '
        message12 = 'احذروا الفوركس والحسابات الوهميه \n كلها كذب وتستهدف الخليج '
        message13 = 'احذروا من اعلانات حسابات الفوركس  \n كلها كذب وسرقة '

        try:
            api.update_status(status = temphash + message)
            print 'message sent'
        except tweepy.TweepError as e:
            print (e.reason)
            pass
        try:
            api.update_status(status=temphash + message2)
            print 'message2 sent'
        except tweepy.TweepError as e:
            print (e.reason)
            pass
        try:
            api.update_status(status=temphash + message3)
            print 'message3 sent'
        except tweepy.TweepError as e:
            print (e.reason)
            pass
        try:
            api.update_status(status=temphash + message4)
            print 'message4 sent'
        except tweepy.TweepError as e:
            print (e.reason)
            pass
        try:
            api.update_status(status=temphash + message5)
            print 'message5 sent'
        except tweepy.TweepError as e:
            print (e.reason)
            pass
        try:
            api.update_status(status=temphash + message6)
            print 'message6 sent'
        except tweepy.TweepError as e:
            print (e.reason)
            pass
        try:
            api.update_status(status=temphash + message7)
            print 'message7 sent'
        except tweepy.TweepError as e:
            print (e.reason)
            pass
        try:
            api.update_status(status=temphash + message8)
            print 'message8 sent'
        except tweepy.TweepError as e:
            print (e.reason)
            pass
        try:
            api.update_status(status=temphash + message9)
            print 'message9 sent'
        except tweepy.TweepError as e:
            print (e.reason)
            pass
        try:
            api.update_status(status=temphash + message10)
            print 'message10 sent'
        except tweepy.TweepError as e:
            print (e.reason)
            pass
        try:
            api.update_status(status=temphash + message11)
            print 'message11 sent'
        except tweepy.TweepError as e:
            print (e.reason)
            pass
        try:
            api.update_status(status=temphash + message12)
            print 'message12 sent'
        except tweepy.TweepError as e:
            print (e.reason)
            pass
        try:
            api.update_status(status=temphash + message13)
            print 'message13 sent'
        except tweepy.TweepError as e:
            print (e.reason)
            pass
        try:
            api.destroy_status
        except:
            pass

        sleep(60)
        # first = first + 3
        # second = second + 3
except:
    pass
