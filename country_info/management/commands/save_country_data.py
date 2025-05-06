import requests
from django.core.management.base import BaseCommand
from django.db import transaction
from country_info.models import *


class Command(BaseCommand):
    help = 'Fetch countries from REST Countries API and populate the database'

    @transaction.atomic
    def handle(self, *args, **options):
        url = 'https://restcountries.com/v3.1/all'
        resp = requests.get(url)
        if resp.status_code != 200:
            self.stderr.write("Failed to fetch data")
            return
        data = resp.json()

        # Create all continents
        all_continents = {cont for item in data for cont in item.get("continents", [])}
        for name in all_continents:
            Continent.objects.get_or_create(name=name)

        # Create countries (without M2M fields)
        code_to_country = {}
        for item in data:
            cca3 = item.get("cca3")
            if not cca3:
                continue

            country = Country.objects.create(
                name_common = item["name"]["common"],
                name_official = item["name"]["official"],
                native_names = item["name"].get("nativeName", {}),
                alt_spellings = item.get("altSpellings", []),

                tld = item.get("tld", []),
                cca2 = item.get("cca2"),
                ccn3 = item.get("ccn3"),
                cca3 = cca3,
                cioc = item.get("cioc"),

                independent = item.get("independent", False),
                status = item.get("status"),
                un_member = item.get("unMember", False),

                idd_root = item.get("idd", {}).get("root"),
                idd_suffixes = item.get("idd", {}).get("suffixes", []),

                region = item.get("region"),
                subregion = item.get("subregion"),
                latlng = item.get("latlng", []),
                landlocked = item.get("landlocked", False),
                area = item.get("area", 0.0),

                capital = item.get("capital", []),
                capital_info = item.get("capitalInfo", {}).get("latlng", []),

                population = item.get("population", 0),
                demonyms = item.get("demonyms", {}),
                gini = item.get("gini", {}),

                fifa = item.get("fifa"),
                timezones = item.get("timezones", []),
                start_of_week = item.get("startOfWeek"),

                car_signs = item.get("car", {}).get("signs", []),
                car_side = item.get("car", {}).get("side"),

                postal_code_format = item.get("postalCode", {}).get("format"),
                postal_code_regex = item.get("postalCode", {}).get("regex"),

                flag_emoji = item.get("flag"),
                flag_png = item.get("flags", {}).get("png"),
                flag_svg = item.get("flags", {}).get("svg"),
                coat_of_arms_png = item.get("coatOfArms", {}).get("png"),
                coat_of_arms_svg = item.get("coatOfArms", {}).get("svg"),

                maps_google = item.get("maps", {}).get("googleMaps"),
                maps_osm = item.get("maps", {}).get("openStreetMaps"),
            )

            for cont_name in item.get("continents", []):
                cont = Continent.objects.get(name=cont_name)
                country.continents.add(cont)

            code_to_country[cca3] = country

        # Now set borders, languages, currencies, translations
        for item in data:
            cca3 = item.get("cca3")
            country = code_to_country.get(cca3)
            if not country:
                continue

            # Add Borders
            for b in item.get("borders", []):
                neigh = code_to_country.get(b)
                if neigh:
                    country.borders.add(neigh)

            # Add Languages
            for code, name in item.get("languages", {}).items():
                lang, _ = Language.objects.get_or_create(code=code, defaults={"name": name})
                country.languages.add(lang)

            # Add Currencies
            for code, info in item.get("currencies", {}).items():
                cur, _ = Currency.objects.get_or_create(
                    code=code,
                    defaults={"name": info.get("name"), "symbol": info.get("symbol")}
                )
                country.currencies.add(cur)

            # Add Translations
            for lang_code, vals in item.get("translations", {}).items():
                Translation.objects.create(
                    country=country,
                    language_code=lang_code,
                    official=vals.get("official"),
                    common=vals.get("common"),
                )

        self.stdout.write(self.style.SUCCESS("Countries successfully fetched and stored."))
        