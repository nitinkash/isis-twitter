# Growth of the Social Networks
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


import pandas as pd
df = pd.read_csv("tweets.csv")

# Extract the people from the tweets
import re
import networkx as nx
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt

times = list(df['time'])
act_time = []
month = []
for time in times:
	dummy = datetime.strptime(time, '%m/%d/%Y %H:%M')
	act_time.append(dummy)
	month.append((dummy.date().month, dummy.date().year))

df['act_time'] = act_time
df['month'] = month
g = nx.Graph()

# Partition dataframe 
month_ = f7(month)
retweets = []
actual_tweets = []
in_set = []
not_in_set =[]
#'''
for mon in month_:
	#print(mon)
	#input()
	
	df1 = df.loc[df['month'] == mon]
	#print(df1)
	#input()
	for user, tweet in zip(df1['username'], df1['tweets']):
		match = re.search(r'^\bRT\b', tweet)
		if match == None:
			actual_tweets.append([user,tweet])
		else:
			retweets.append([user,tweet])
	print(len(actual_tweets))
	# Find the mentions
	for user, tweet in actual_tweets:
		match = re.findall(r'@\w*', tweet)
		if match != []:
			for name in match:
				if (name[1:] in df1['username'].unique()) and (user != name[1:]):
					in_set.append([user, name[1:]])
				elif user != name[1:]:
					not_in_set.append([user, name[1:]])

	# Visualizations in nx
	all_users = [item for i in in_set for item in i] 
	fanboys = list(set(all_users))
	#print(fanboys)
	#input()
	for i in fanboys: #Add node already exists condition
		nodes = g.nodes()
		if i not in nodes:
			#print("Adding node ", i)
			g.add_node(i)
	edges = {}
	occ_count = Counter(map(tuple, in_set)) #Map in_set to a tuple
	for (sender, receiver), count in occ_count.items():
		edges = g.edges()
		if (sender, receiver) not in edges:		
			g.add_edge(sender, receiver) 

	#Export to gexf for gephi
	file_name = "mentions_network_" + str(mon)+'_.gexf'
	
	if len(g.nodes()) > 0:
		nx.write_gexf(g, file_name)		
		#nx.draw_spring(g, with_labels=True)
		#plt.draw()
		#plt.show()

