from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

url = u'http://twitter.com/' + 'nikashyap' +'?page=%s'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
 
for x in range(10*10000):
	f = urlopen(url % x)
	soup = BeautifulSoup(f.read(), "html")
	f.close()
	tweets = soup.findAll('span', {'class': 'entry-content'})
	dates = soup.findAll('span',{'class': 'published timestamp'})
	print(tweets)
	if tweets == None:
		break

