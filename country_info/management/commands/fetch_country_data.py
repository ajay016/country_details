from django.core.management.base import BaseCommand
import requests
import json
import os


class Command(BaseCommand):
    help = 'Fetches country data from the API and saves it to the database'

    def handle(self, *args, **kwargs):
        url = 'https://restcountries.com/v3.1/all'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Ensure the directory exists
            os.makedirs('country_info', exist_ok=True)

            with open('country_info/countries.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            self.stdout.write(self.style.SUCCESS('Successfully fetched and saved country data.'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data. Status code: {response.status_code}'))
