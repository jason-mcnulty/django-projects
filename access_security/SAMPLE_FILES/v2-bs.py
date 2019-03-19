# https://dev.to/ayushsharma/a-guide-to-web-scraping-in-python-using-beautifulsoup-1kgo
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth



url = 'https://twitter.com/TheOnion'
data = requests.get(url, verify=False)

all_tweets = []
html = BeautifulSoup(data.text, 'html.parser')






timeline = html.select('#timeline li.stream-item')
for tweet in timeline:
    tweet_id = tweet['data-item-id']
    tweet_text = tweet.select('p.tweet-text')[0].get_text()
    all_tweets.append({"id": tweet_id, "text": tweet_text})


print(all_tweets)
