from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('country-list/', views.CountryListAPIView.as_view(), name='country_list'),
]