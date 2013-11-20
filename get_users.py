import tweepy
import json
import simplejson
from array import *
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="5PXRUCe0QNl2UXTlcIiYCA"
consumer_secret="p2FClXOwzO4yvAM2oAKcElRNk5WLsenJm73cFkTb4o"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token="166457267-LVzoV1Y2W7y2aImys885YtYX4V1WY7YNkUzouYod"
access_token_secret="h4Qmc7UyLOTHeB25q6slF5LTw5cDxXSIz3nND5Xr906vn"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out

class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print 'Ran on_status'

    def on_error(self, status_code):
        print 'Error: ' + repr(status_code)
        return False

    def on_data(self, data):
        print data
        return True
    
user_ids = []
# print len(user_ids)
#use json to load user ids and then use that to get users from twitter
with open("current_trends.json") as json_file:
    for json_line in json_file:
        if len(user_ids) > 99:
            # print user_ids
            users_info = api.lookup_users(user_ids=user_ids)
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
users_info = api.lookup_users(user_ids=user_ids)
for user_info in users_info:
    print user_info.__getstate__()

# print dict(zip([(x.screen_name, x.id_str) for x in l], [x.id_str for x in l]))




