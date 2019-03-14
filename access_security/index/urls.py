from django.urls import path

from . import views


app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.citrix, name='citrix'),
    path('', views.pulse_secure, name='pulse_secure'),
]
