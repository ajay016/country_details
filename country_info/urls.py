from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_country_data/', views.get_country_data, name='get_country_data'),
]