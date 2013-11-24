import tweepy
import json
import csv

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

with open('features.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

with open("sample_users.json") as user_json_file:
    for user_json_line in user_json_file:
        user_json = json.loads(user_json_line)
        print (user_json)
#         print api.get_timeline(id = user_json['id'])

#spamwriter.writerow(['Spam'] * 5 + ['Baked,Beans'])