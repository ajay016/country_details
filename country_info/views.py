from django.shortcuts import render
from django.core.paginator import Paginator
import requests
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import *
from country_info_api.serializers import CountrySerializer


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
