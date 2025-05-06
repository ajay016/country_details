from django.shortcuts import render
from django.core.paginator import Paginator
import requests
import json
from django.http import JsonResponse
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
