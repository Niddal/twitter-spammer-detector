import tweepy
import json
import simplejson
from array import *
from twitter import *
import jsonpickle
import inspect
from twython import Twython
import os
from tweepy.parsers import RawJsonParser
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application"s Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="5PXRUCe0QNl2UXTlcIiYCA"
consumer_secret="p2FClXOwzO4yvAM2oAKcElRNk5WLsenJm73cFkTb4o"

# The access tokens can be found on your applications"s Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token="166457267-LVzoV1Y2W7y2aImys885YtYX4V1WY7YNkUzouYod"
access_token_secret="h4Qmc7UyLOTHeB25q6slF5LTw5cDxXSIz3nND5Xr906vn"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api_raw = tweepy.API(auth, parser=RawJsonParser())
api = tweepy.API(auth)

twitter_auth = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

twython_auth = Twython(consumer_key, consumer_secret, access_token, access_token_secret)


# If the authentication was successful, you should
# see the name of the account print out

class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print "Ran on_status"

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True

    def on_data(self, data):
        print data
        return True
    
user_ids = []
# print len(user_ids)
#use json to load user ids and then use that to get users from twitter
with open("sample.json") as json_file:
    for json_line in json_file:
        if len(user_ids) > 99:
            # print user_ids
            users_info = api_raw.lookup_users(user_ids=user_ids)
            for user_info in users_info:
                print user_info.__getstate__()
            user_ids = []
        try:
            json_data = json.loads(json_line)
            user_ids.append(json_data["user"]["id"])
            user_ids = list(set(user_ids))
        except ValueError:
            value_error = 1

#cleanup code
# print user_ids  
users_info = json.loads(api_raw.lookup_users(user_ids=user_ids))

# print inspect.getmembers(api)

# users_info = twitter_auth.users.lookup(screen_name="BCCI,littlecegian07", include_entities=1)
for user_info in users_info:
    # pickled = jsonpickle.encode(user_info)
    # user_json_object = json.loads(pickled)
    user_json_string = json.dumps(user_info, indent=4, sort_keys=True)
    user_id = user_info["id"]
    directory = "data_collected/" + str(user_id)
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(directory)
    user_details = open('user.json','w')
    user_details.write(user_json_string)
    user_details.close()
    timeline_tweets = api.user_timeline(id=user_id)
    for tweet in timeline_tweets:
        print json.dumps(tweet)
    # print json.dumps(jsonpickle.encode(api.user_timeline(id=user_id)), indent=4, sort_keys=True)

# print api.me().__getstate__
# print dict(zip([(x.screen_name, x.id_str) for x in l], [x.id_str for x in l])


