from django.shortcuts import render, HttpResponse

# Create your views here.
# def pulse_secure(request):
#     return HttpResponse("This is the Pulse Secure page.")
def pulse_secure(request):
    return render(request, 'pulse_secure/index.html')


#
