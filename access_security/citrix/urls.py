from django.urls import path

from . import views


app_name = 'citrix'

urlpatterns = [
    path('', views.citrix, name='citrix'),
]
