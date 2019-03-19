import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
from django.shortcuts import render, HttpResponse


# Create your views here.
# def pulse_secure(request):
#     return HttpResponse("This is the Pulse Secure page.")
def pulse_secure(request):


    ###########################################################################################
    # vappsavpn01.mgmt.wellpoint.com
    ###########################################################################################
    ssl = 'https://'
    host = 'vappsavpn01-int.internal.das'
    check = '/dana-na/healthcheck/healthcheck.cgi?status=all'

    url = ssl + host + check
    page_response = requests.get(url, verify=False)
    page_content = BeautifulSoup(page_response.text, "html.parser")

    ###########################################################################################
    # vappsavpn02.mgmt.wellpoint.com
    ###########################################################################################
    ssl = 'https://'
    host = 'vappsavpn02-int.internal.das'
    check = '/dana-na/healthcheck/healthcheck.cgi?status=all'

    url = ssl + host + check
    page_response = requests.get(url, verify=False)
    page_content = BeautifulSoup(page_response.text, "html.parser")



    ###########################################################################################
    # vappsavpn03.mgmt.wellpoint.com
    ###########################################################################################
    ssl = 'https://'
    host = 'vappsavpn03-int.internal.das'
    check = '/dana-na/healthcheck/healthcheck.cgi?status=all'

    url = ssl + host + check
    page_response = requests.get(url, verify=False)
    page_content = BeautifulSoup(page_response.text, "html.parser")


    ###########################################################################################
    # moppsavpn01.mgmt.wellpoint.com
    ###########################################################################################
    ssl = 'https://'
    host = 'moppsavpn01-int.internal.das'
    check = '/dana-na/healthcheck/healthcheck.cgi?status=all'

    url = ssl + host + check
    page_response = requests.get(url, verify=False)
    page_content = BeautifulSoup(page_response.text, "html.parser")


    ###########################################################################################
    # moppsavpn02.mgmt.wellpoint.com
    ###########################################################################################
    ssl = 'https://'
    host = 'moppsavpn02-int.internal.das'
    check = '/dana-na/healthcheck/healthcheck.cgi?status=all'

    url = ssl + host + check
    page_response = requests.get(url, verify=False)
    page_content = BeautifulSoup(page_response.text, "html.parser")


    ###########################################################################################
    # moppsavpn03.mgmt.wellpoint.com
    ###########################################################################################
    ssl = 'https://'
    host = 'moppsavpn03-int.internal.das'
    check = '/dana-na/healthcheck/healthcheck.cgi?status=all'

    url = ssl + host + check
    page_response = requests.get(url, verify=False)
    page_content = BeautifulSoup(page_response.text, "html.parser")




    pulse_secure = {
        'host_name01': "vappsavpn01",
        "results01" : (page_content),
        'host_name02': "vappsavpn02",
        "results02" : (page_content),
        'host_name03': "vappsavpn03",
        "results03" : (page_content),
        'host_name_mo01': "moppsavpn01",
        "results_mo01" : (page_content),
        'host_name_mo02': "moppsavpn02",
        "results_mo02" : (page_content),
        'host_name_mo03': "moppsavpn03",
        "results_mo03" : (page_content),
    }

    return render(request, 'pulse_secure/index.html', context=pulse_secure)


#
