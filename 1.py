#The pobjective of this is to build a bot so that we can identify new ISIS fanboys

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

# Visualizations in nx
import networkx as nx
all_users = [item for i in in_set for item in i] #Check comprehension!!!
fanboys = list(set(all_users))
g = nx.Graph()
for i in fanboys:
	g.add_nodes(i)
#Using a weighted edge to denote relationships based on the number of tweets
edges = {}
from collections import Counter
occ_count = Counter(map(tuple, in_set)) #Map in_set to a tuple
for (sender, receiver), count in occ_count.items():
	if (receiver, sender) in edges.keys():
		edges[(receiver, sender)] = edges[(receiver, sender)] + count
	else:
		edges[(sender, receiver)] = count
        
for (sender, receiver), count in edges.items():
	g.add_edge(sender, receiver, weight=count)

#Export to gexf fro gephi
nx.write_gexf(g, "mentions_network")

# Exploration using tweepy( Modify to web scraping method)

		
	

for i in len(first.tweets):
		
