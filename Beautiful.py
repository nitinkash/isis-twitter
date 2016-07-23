import pandas as pd
df = pd.read_csv("tweets.csv")

# Extract the people from the tweets
import re
#First remove RTs
retweets = []
actual_tweets = []
for user, tweet in zip(df['username'], df['tweets']):
    match = re.search(r'^\bRT\b', tweet)
    if match == None:
        actual_tweets.append([user,tweet])
    else:
        retweets.append([user,tweet])

# Find the mentions
in_set = []
not_in_set =[]
for user, tweet in actual_tweets:
	match = re.findall(r'@\w*', tweet)
	if match != []:
		for name in match:
	import time
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

# Replace USERNAME with your twitter username
url = u'http://twitter.com/USERNAME?page=%s'

for x in range(10*10000):
    f = urlopen(url % x)
    soup = BeautifulSoup(f.read())
    f.close()
   # print soup #WHAT'S GOING ON?
    tweets = soup.findAll('span', {'class': 'entry-content'})
    dates = soup.findAll('span',{'class': 'published timestamp'})

    for index, tweet in enumerate(tweets):
	print "<h3>",dates[index].renderContents(),"</h3><p>",tweet.renderContents(),"</p>"
#	print tweet.renderContents()


    if len(tweets) == 0:
        break
    # being nice to twitter's servers
    time.sleep(5)		if (name[1:] in df['username'].unique()) and (user != name[1:]):
				in_set.append([user, name[1:]])
			elif user != name[1:]:
				not_in_set.append([user, name[1:]])

# Visualizations in nx
import networkx as nx
all_users = [item for i in in_set for item in i] #Check comprehension!!!
fanboys = list(set(all_users))

import time
from urllib2 import urlopen
from bs4 import BeautifulSoup

# Replace USERNAME with your twitter username
for i in fanboys:
	url = u'http://twitter.com/'+str(i)+ '?page=%s'	
	#url = u'http://twitter.com/USERNAME?page=%s'

	for x in range(10*10000):
	    f = urlopen(url % x)
	    soup = BeautifulSoup(f.read())
	    f.close()
	   # print soup #WHAT'S GOING ON?
	    tweets = soup.findAll('span', {'class': 'entry-content'})
	    dates = soup.findAll('span',{'class': 'published timestamp'})

	    for index, tweet in enumerate(tweets):
		print "<h3>",dates[index].renderContents(),"</h3><p>",tweet.renderContents(),"</p>"
	#	print tweet.renderContents()


	    if len(tweets) == 0:
		break
	    # being nice to twitter's servers
	    time.sleep(5)
