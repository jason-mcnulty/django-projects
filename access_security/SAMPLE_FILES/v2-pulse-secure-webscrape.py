from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
from requests.auth import HTTPBasicAuth

ssl = 'https://'
host = 'vappsavpn01-int.internal.das'
check = '/dana-na/healthcheck/healthcheck.cgi?status=all'

# Here, we're just importing both Beautiful Soup and the Requests library
url = ssl + host + check
# this is the url that we've already determined is safe and legal to scrape from.

#functon to pull username from txt file on local machine
def get_username():
    f = open('/Users/AC89458/Documents/ad_username.txt', 'r')
    my_username = f.read().strip()
    return my_username
    f.close()

#functon to pull password from txt file on local machine
def get_passwd():
    f = open('/Users/AC89458/Documents/ad_pausewd.txt', 'r')
    my_passwd = f.read().strip()
    return my_passwd
    f.close()

#assigning the username and password to a variable by calling upon the function
username = get_username()
passwd = get_passwd()

page_response = requests.get(url,auth=HTTPBasicAuth((username), (passwd)), verify=False)

# page_response = requests.get(url, timeout=5)
# here, we fetch the content from the url, using the requests library
page_content = BeautifulSoup(page_response.content, "html.parser")
#we use the html parser to parse the url content and store it in a variable.


# tree = ET.fromstring(page_content)
# print (tree)

print (page_content)
