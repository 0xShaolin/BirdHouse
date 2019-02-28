##### this is the template in case you would like to modify your
##### own version of birdhouse

import requests, os

user = 'shaolincnc' # change this to whichever username

def Tweet(user,tcode):
	r = requests.get('https://twitter.com/'+user+'/status/'+tcode)
	if r.status_code == 200:
		tweet = r.content.split('on Twitter: \&quot;')[1].split('\&quot;&quot;,&quot;')[0]
	else:
		tweet = 'Encountered error: '+str(r.status_code)
	return tweet

def tweetCodes(user):
	r = requests.get('https://twitter.com/'+user)
	if r.status_code == 200:
		codes = []
		for c in r.content.split('data-item-id=\"'):
			if 'stream' not in c.split('\"\nid=\"stream-item-tweet')[0]:
				codes.append(c.split('\"\nid=\"stream-item-tweet')[0])
	else:
		code = 'Encountered error: '+str(r.status_code)
	return codes

codes = tweetCodes(user)
try:
	print Tweet(user,codes[-1:][0])
except:
	pass

while True:
	try:
		t = codes[-1:]
		if 'error' not in tweetCodes(user):
			for c in tweetCodes(user):
				if c not in codes:
					codes.append(c)

			if codes[-1:] and t != codes[-1:]:
				latest = Tweet(user,codes[-1:][0]) # this will get the most recent tweet (and print it later on)
				os.system(latest)
		else:
			print tweetCodes(user) # this will print "Encountered error: <error-code>"
	except KeyboardInterrupt:
		exit('\nSafely exiting program...')
