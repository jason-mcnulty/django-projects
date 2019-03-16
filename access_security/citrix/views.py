import requests
from requests.auth import HTTPBasicAuth
import json

from django.shortcuts import render, HttpResponse

# Create your views here.
# def citrix(request):
#     return HttpResponse("This is the Citrix page citrix.views.py.")

def CTXZeroOne(request):

    ssl = 'https://'
    host1 = 'va10pctxns001.mgmt.wellpoint.com'
    api = '/nitro/v1/stat/'
    service = 'aaa'

    ###########################################################################################
    # va10pctxns001.mgmt.wellpoint.com
    ###########################################################################################
    #assigning the variable url to the URL of the API
    url =  ssl + host1 + api + service

    #assigning the username and password to a variable by calling upon the function
    username = 'ac89458'
    passwd = 'Jayantliz2'

    #this is where the magic happens...
    myResponse = requests.get(url,auth=HTTPBasicAuth((username), (passwd)), verify=False)
    jData = json.loads(myResponse.content)

    for aaa_id,aaa_info in jData.items():
        print("\nAAA ID:", aaa_id)

    for key in aaa_info:
        print(key + ':', aaa_info[key])

    CTXZeroOne = {
    'aaacuricaonlyconn' : aaa_info['aaacuricaonlyconn'],
    'aaacuricasessions' : aaa_info['aaacuricasessions'],
    }



    return render(request, 'citrix/index.html', context=CTXZeroOne)
