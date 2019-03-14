from django.urls import path

from . import views

urlpatterns = [
    path('', views.pulse_secure),
]
