from django.shortcuts import render, HttpResponse

# Create your views here.
# def citrix(request):
#     return HttpResponse("This is the Citrix page citrix.views.py.")


def citrix(request):
    return render(request, 'citrix/index.html')
