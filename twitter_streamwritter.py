# Finding topics of interest by using the filtering capablities it offers.
import twitter
import json
import sys
import csv

csvfile = open('twitter_stream_dump.csv', 'a')
csvwriter = csv.writer(csvfile)
 
# == OAuth Authentication ==
# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "Keys and tokens")
 # PUT YOUR KEYS AND SECRETS IN HERE, IT WONT WORK WITHOUT YOUR KEYS FROM TWITTER !!!!!
consumer_key="BxeiCgH3Y2ApUMZRHXMrrC712"
consumer_secret="B0Z1DixnRUVrGpzMs4A8C0Dc0B56ytLRhtNcfdZGbX726ZTewk"
 
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="19191961-i5K5HnfgLp0f5o9rH0yr5PMEsHGxPwJM8cUyEuWaB"
access_token_secret="5dByulUu4KXvErsOYR2nSFTUYCFUdwsGpRVZ6lLu4PINQ"
 
auth = twitter.oauth.OAuth(access_token, access_token_secret,consumer_key, consumer_secret)
twitter_api = twitter.Twitter(auth=auth)
# Query terms
q = 'cameronmustgo' # Comma-separated list of terms, start with something busy to test your script, then once you know its working put your hashtags in, max 400 tags
print >> sys.stderr, 'Filtering the public timeline for track="%s"' % (q,)
# Reference the self.auth parameter
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
# See https://dev.twitter.com/docs/streaming-apis
stream = twitter_stream.statuses.filter(track=q)
# For illustrative purposes, when all else fails, search for Justin Bieber
# and something is sure to turn up (at least, on Twitter)
# note that stream is a special never ending list so this loops foreeeeeevveeeeeer
# to stop it type CMD-C at the terminal where its running
for tweet in stream:
	# what is this thing called a tweet?
	# its a structured object in JSON format. We can treat this as a python dictionary - http://learnpythonthehardway.org/book/ex39.html
	# sometimes it helps to dump an entire tweet using the line below so you can see the names of the fields
	print tweet['user']['screen_name']
	#The line below defines the varible from above  
	user = tweet['user']['screen_name'].encode('utf-8')
	print tweet['created_at']
	created_at = tweet['created_at']
	print tweet['text']
	text = tweet['text'].encode('utf-8')
	csvwriter.writerow([user, text, created_at])          
