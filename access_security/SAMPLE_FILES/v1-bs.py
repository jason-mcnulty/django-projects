#python 3
from bs4 import BeautifulSoup
import urllib.request
page = urllib.request.urlopen('http://example.com/')
text = page.read().decode("utf8")


soup = BeautifulSoup(text, 'html.parser')




for link in soup.find_all('div'):
    print(link)
