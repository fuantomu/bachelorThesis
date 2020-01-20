# Finding topics of interest by using the filtering capablities it offers.
import twitter
import json
import sys
import csv

csvfile = open('YOUR DATA BASE NAME.csv','a')
csvwriter = csv.writer(csvfile)
 
# == OAuth Authentication ==
# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "Keys and tokens")
 # PUT YOUR KEYS AND SECRETS IN HERE, IT WONT WORK WITHOUT YOUR KEYS FROM TWITTER !!!!!
consumer_key="YOUR KEY"
consumer_secret="YOUR CONSUMER SECRET"
 
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="67271475-y4QNnALrD918v1Z4kKKOoTc6bvABtDz6LqdBlp0Pp"
access_token_secret="tSz8Ly6gwsi2maaxTU3CTrr8XlhzTYWpox7z6Pxh52zOC"
 
auth = twitter.oauth.OAuth(access_token, access_token_secret,consumer_key, consumer_secret)
twitter_api = twitter.Twitter(auth=auth)
# Query terms
q = 'YOUR HASHTAG' # Comma-separated list of terms, start with something busy to test your script, then once you know its working put your hashtags in, max 400 tags
print >> sys.stderr, 'Filtering the public timeline for track="%s"' % (q,)
# Reference the self.auth parameter
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
# See https://dev.twitter.com/docs/streaming-apis
stream = twitter_stream.statuses.filter(track=q)
# For illustrative purposes, when all else fails, search for a relevant topic such as Madonna
# and something is sure to turn up (at least, on Twitter)
# note that stream is a special never ending list so this loops non stop
# to stop it type CMD-C at the terminal where its running
for tweet in stream:
	# what is this thing called a tweet?
	# its a structured object in JSON format. We can treat this as a python dictionary - http://learnpythonthehardway.org/book/ex39.html
	# sometimes it helps to dump an entire tweet using the line below so you can see the names of the fields
	# print json.dumps(tweet, indent=1')
	print tweet['text']
	
	csvwriter.writerow([tweet['text'].encode('utf-8'),tweet['user']['screen_name'].encode('utf-8'),tweet['created_at']])
	