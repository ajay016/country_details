from django.shortcuts import render
import requests
import json
from django.http import JsonResponse



def home(request):
    return render(request, 'country_info/home.html')




    