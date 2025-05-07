from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import requests
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from country_info_api.serializers import CountrySerializer



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your actual home view name
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'country_info/authentication/login_user.html')


def logout_user(request):
    logout(request)
    return redirect('login_user')


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register_user')  # Redirect to the registration page to show the message

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('register_user')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register_user')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        messages.success(request, 'User registered successfully.')
        return redirect('login_user')  # Redirect to the login page after successful registration

    return render(request, 'country_info/authentication/registration.html')


@login_required(login_url='login_user')
def home(request):
    qs = Country.objects.all()

    # 🔍 Search filter
    search_query = request.GET.get('search', '').strip()
    if search_query:
        qs = qs.filter(name_common__icontains=search_query)

    # 📄 Pagination
    per_page = 10 
    page_number = request.GET.get('page', 1)
    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(page_number)

    # 🔄 Serialize only the current page’s items
    serializer = CountrySerializer(page_obj.object_list, many=True)

    return render(request, 'country_info/index.html', {
        'countries':    serializer.data,
        'page_obj':     page_obj,
        'is_paginated': page_obj.has_other_pages(),
        # you can pass the search string back if you need it explicitly:
        'search':       search_query,
    })


def country_details(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    
    context = {
        'countries': serializer.data
    }
    return render(request, 'country_info/index.html', context)


def country_details_json(request, cca3):
    cca3 = cca3.upper()
    country = get_object_or_404(Country, cca3=cca3)

    # Get same-region countries excluding the selected one
    same_region_countries = Country.objects.filter(region=country.region).exclude(cca3=cca3)
    regional_country_names = list(same_region_countries.values_list('name_common', flat=True))

    # Get languages spoken by this country
    language_names = list(country.languages.values_list('name', flat=True))

    data = {
        'same_region_countries': regional_country_names,
        'languages': language_names,
    }

    return JsonResponse(data, status=200)
