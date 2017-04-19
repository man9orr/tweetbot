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


trends1 = api.trends_place(23424938)


i = 50 * 50
while i < 5000:
    clearing_file = open('trends.txt', 'w')
    erase = clearing_file.write(" ")
    clearing_file.close()
    for trend in trends1[0]['trends']:
        print (trend['name'])

        uopen2 = open('trends.txt', 'a')
        uopen2.write(trend['name'] + '\n')
        uopen2.close()
    sleep(180)
    i = i + 1