import requests
from requests.auth import HTTPBasicAuth
import json

from django.shortcuts import render, HttpResponse

# Create your views here.
# def citrix(request):
#     return HttpResponse("This is the Citrix page citrix.views.py.")

def citrix(request):
    ###########################################################################################
    # va10pctxns001.mgmt.wellpoint.com
    ###########################################################################################
    ssl = 'https://'
    host1 = 'va10pctxns001.mgmt.wellpoint.com'
    api = '/nitro/v1/stat/'
    service = 'aaa'
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
    ###########################################################################################
    ###########################################################################################


    ###########################################################################################
    # va10pctxns002.mgmt.wellpoint.com
    ###########################################################################################
    ssl = 'https://'
    host1 = 'va10pctxns002.mgmt.wellpoint.com'
    api = '/nitro/v1/stat/'
    service = 'aaa'
    #assigning the variable url to the URL of the API
    url =  ssl + host1 + api + service
    #assigning the username and password to a variable by calling upon the function
    username = 'ac89458'
    passwd = 'Jayantliz2'
    #this is where the magic happens...
    myResponse = requests.get(url,auth=HTTPBasicAuth((username), (passwd)), verify=False)
    jData = json.loads(myResponse.content)

    for two_id,two_info in jData.items():
        print("\nAAA ID:", two_id)

    for key in two_info:
        print(key + ':', two_info[key])
    ###########################################################################################
    ###########################################################################################

    ###########################################################################################
    # va10pctxns003.mgmt.wellpoint.com
    ###########################################################################################
    ssl = 'https://'
    host1 = 'va10pctxns003.mgmt.wellpoint.com'
    api = '/nitro/v1/stat/'
    service = 'aaa'
    #assigning the variable url to the URL of the API
    url =  ssl + host1 + api + service
    #assigning the username and password to a variable by calling upon the function
    username = 'ac89458'
    passwd = 'Jayantliz2'
    #this is where the magic happens...
    myResponse = requests.get(url,auth=HTTPBasicAuth((username), (passwd)), verify=False)
    jData = json.loads(myResponse.content)

    for three_id,three_info in jData.items():
        print("\nAAA ID:", three_id)

    for key in three_info:
        print(key + ':', three_info[key])
    ###########################################################################################
    ###########################################################################################

    ###########################################################################################
    # va10pctxns004.mgmt.wellpoint.com
    ###########################################################################################
    ssl = 'https://'
    host1 = 'va10pctxns004.mgmt.wellpoint.com'
    api = '/nitro/v1/stat/'
    service = 'aaa'
    #assigning the variable url to the URL of the API
    url =  ssl + host1 + api + service
    #assigning the username and password to a variable by calling upon the function
    username = 'ac89458'
    passwd = 'Jayantliz2'
    #this is where the magic happens...
    myResponse = requests.get(url,auth=HTTPBasicAuth((username), (passwd)), verify=False)
    jData = json.loads(myResponse.content)

    for four_id,four_info in jData.items():
        print("\nAAA ID:", four_id)

    for key in four_info:
        print(key + ':', four_info[key])
    ###########################################################################################
    ###########################################################################################

    ###########################################################################################
    # va10pctxns004.mgmt.wellpoint.com
    ###########################################################################################
    ssl = 'https://'
    host1 = 'va10pctxns005.mgmt.wellpoint.com'
    api = '/nitro/v1/stat/'
    service = 'aaa'
    #assigning the variable url to the URL of the API
    url =  ssl + host1 + api + service
    #assigning the username and password to a variable by calling upon the function
    username = 'ac89458'
    passwd = 'Jayantliz2'
    #this is where the magic happens...
    myResponse = requests.get(url,auth=HTTPBasicAuth((username), (passwd)), verify=False)
    jData = json.loads(myResponse.content)

    for five_id,five_info in jData.items():
        print("\nAAA ID:", five_id)

    for key in five_info:
        print(key + ':', five_info[key])
    ###########################################################################################
    ###########################################################################################



    citrix = {
    'host_name01': "va10pctxns001",
    'aaacuricaonlyconn01' : aaa_info['aaacuricaonlyconn'],
    'aaacuricasessions01' : aaa_info['aaacuricasessions'],
    'host_name02': "va10pctxns002",
    'aaacuricaonlyconn02' : two_info['aaacuricaonlyconn'],
    'aaacuricasessions02' : two_info['aaacuricasessions'],
    'host_name03': "va10pctxns003",
    'aaacuricaonlyconn03' : three_info['aaacuricaonlyconn'],
    'aaacuricasessions03' : three_info['aaacuricasessions'],
    'host_name04': "va10pctxns004",
    'aaacuricaonlyconn04' : four_info['aaacuricaonlyconn'],
    'aaacuricasessions04' : four_info['aaacuricasessions'],
    'host_name05': "va10pctxns005",
    'aaacuricaonlyconn05' : four_info['aaacuricaonlyconn'],
    'aaacuricasessions05' : four_info['aaacuricasessions'],
    }

    return render(request, 'citrix/index.html', context=citrix)
