from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('country_details/', views.country_details, name='country_details'),
    path('view-country-details/<str:cca3>', views.country_details_json, name='view_country_details'),
]