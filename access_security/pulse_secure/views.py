import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
from django.shortcuts import render, HttpResponse


# Create your views here.
# def pulse_secure(request):
#     return HttpResponse("This is the Pulse Secure page.")
def pulse_secure(request):


    ###########################################################################################
    # va10pctxns001.mgmt.wellpoint.com
    ###########################################################################################
    ssl = 'https://'
    host = 'vappsavpn01-int.internal.das'
    check = '/dana-na/healthcheck/healthcheck.cgi?status=all'

    # Here, we're just importing both Beautiful Soup and the Requests library
    url = ssl + host + check
    # this is the url that we've already determined is safe and legal to scrape from.

    username = 'ac89458'
    passwd = 'Jayantliz2'
    #functon to pull username from txt file on local machine
    # def get_username():
    #     f = open('/Users/AC89458/Documents/ad_username.txt', 'r')
    #     my_username = f.read().strip()
    #     return my_username
    #     f.close()

    #functon to pull password from txt file on local machine
    # def get_passwd():
    #     f = open('/Users/AC89458/Documents/ad_pausewd.txt', 'r')
    #     my_passwd = f.read().strip()
    #     return my_passwd
    #     f.close()

    #assigning the username and password to a variable by calling upon the function
    # username = get_username()
    # passwd = get_passwd()

    page_response = requests.get(url,auth=HTTPBasicAuth((username), (passwd)), verify=False)

    # page_response = requests.get(url, timeout=5)
    # here, we fetch the content from the url, using the requests library
    page_content = BeautifulSoup(page_response.content, "html.parser")
    #we use the html parser to parse the url content and store it in a variable.

    print (page_content)
    pulse_secure = {

    'host_name01' : "vappsavpn01",

    'page_content' : 'page_content'

    }




















    return render(request, 'pulse_secure/index.html', context=pulse_secure)


#
