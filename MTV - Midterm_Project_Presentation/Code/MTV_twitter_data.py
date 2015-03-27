# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:48:08 2015

@author: Tijo
"""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
APP_KEY = "IVX2Y4peHIip8BUw6STzOW437"
APP_SECRET = "Fpww5h7I2AgA9jPolXO4OiB0fGuMqOfoXguwJ9K465FPkzTwJK"
OAUTH_TOKEN = "3027109314-3dO3hoz12aLYGVUlf5I76hceKU8FZFUCtlbQVMx"
OAUTH_TOKEN_SECRET = "Maquv9tPwISjmOvYvurSUXkoArtWYXKQ78muRF60Aa9ra"
f=open(r"..\data\Tweet.tsv",'w')
class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        f=open(r"..\data\Tweet.tsv",'a')
        result=json.loads(data,encoding="utf-8")
        #print json.dumps(result,sort_keys=True,indent=4)
        coordinates = result['coordinates']
        location= result['user']['location']
        #print unicode(location).encode('utf-8')
        if coordinates is not None or (location is not None and str(unicode(location).encode('utf-8'))):
            date = result['created_at']
            text = result['text']
            if coordinates is not None:
                coordinates=result['coordinates']['coordinates']
            f.write(str(unicode(coordinates).encode('utf-8'))+"\t"+unicode(text).encode('utf-8')+"\t"+str(unicode(date).encode('utf-8'))+"\t"+unicode(location).encode('utf-8')+"\n")
        return True
    f.close()
    def on_error(self, status):
        print status


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(APP_KEY, APP_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream = Stream(auth, l)
    stream.filter(track=['ferrari','Ford','Nissan'],languages=['en'])
