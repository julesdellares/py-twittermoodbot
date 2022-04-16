#importing some thing from the tweepy library

#creates a "firehose" of tweets based on certain keywords or hashtags
from tweepy.streaming import StreamListener
#authenticatess
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

#class to allow us to print the tweets
class StdOutListener(StreamListener):
    #takes in data from stream listener
    def on_data(self, data):
        print(data)
        return True
    #if an error is encountered this will print that error message (status) to the screen
    def on_error(self, status):
        print(status)


#create and object fromt he StdOutListener
if __name__ == "__main__":

    listener = StdOutListener()
    #"login"
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)
    #if tweet contains opjects in the [], it will add them to the string
    stream.filter(track=[])
