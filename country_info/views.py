from django.shortcuts import render
import requests
import json
from django.http import JsonResponse



def home(request):
    return render(request, 'country_info/home.html')


def get_country_data(request):
    url = 'https://restcountries.com/v3.1/all'
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        with open('country_info/countries.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch data from API'}, status=response.status_code)
