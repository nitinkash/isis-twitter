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
			if (name[1:] in df['username'].unique()) and (user != name[1:]):
				in_set.append([user, name[1:]])
			elif user != name[1:]:
				not_in_set.append([user, name[1:]])

all_users = [item for i in in_set for item in i] #Check comprehension!!!
fanboys = list(set(all_users))

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Replace USERNAME with your twitter username
for fanboy in fanboys:
	url = u'http://twitter.com/' + str(fanboy) +'?page=%s'
	for x in range(10*10000):
		f = urlopen(url % x)
		soup = BeautifulSoup(f.read())
		f.close()
		tweets = soup.findAll('span', {'class': 'entry-content'})
		dates = soup.findAll('span',{'class': 'published timestamp'})
		print(soup)	
		#print(tweets)	
		# being nice to twitter's servers
		#time.sleep(5)		

