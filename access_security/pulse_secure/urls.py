from django.urls import path

from . import views
app_name = 'pulse_secure'

urlpatterns = [
    path('', views.pulse_secure, name='pulse_secure'),
]
