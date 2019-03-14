# from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return render(request, 'index/index.html')

def citrix(request):
    return render(request, 'citrix/index.html')

def pulse_secure(request):
    return render(request, 'pulse_secure/index.html')
