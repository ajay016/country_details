from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('country-list/', views.CountryListAPIView.as_view(), name='country_list'),
    path('country-details/<str:cca3>/', views.CountryDetailView.as_view(), name='country_details'),
    path('create-country/', views.CreateCountryView.as_view(), name='create_country'),
    path('update-country/<str:cca3>', views.CountryUpdateAPIView.as_view(), name='update_country'),
    path('delete-country/<str:cca3>', views.CountryDeleteAPIView.as_view(), name='delete_country'),
]