from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db import transaction
from country_info.models import *
from .serializers import *



class CountryListAPIView(APIView):
    def get(self, request):
        names = list(Country.objects.values_list('name_common', flat=True))
        return Response(names, status=status.HTTP_200_OK)


class CountryDetailView(APIView):
    def get(self, request, cca3):
        try:
            country = Country.objects.get(cca3=cca3.upper())
            serializer = CountrySerializer(country)
            return Response(serializer.data)
        except Country.DoesNotExist:
            return Response({"error": "Country not found"}, status=404)


class CreateCountryView(APIView):
    @transaction.atomic
    def post(self, request):
        data = request.data
        cca3 = data.get("cca3")

        if not cca3:
            return Response({"error": "Missing 'cca3' code."}, status=status.HTTP_400_BAD_REQUEST)

        if Country.objects.filter(cca3=cca3).exists():
            return Response({"error": "Country with this cca3 already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Create main country object
        country = Country.objects.create(
            name_common = data["name"]["common"],
            name_official = data["name"]["official"],
            native_names = data["name"].get("nativeName", {}),
            alt_spellings = data.get("altSpellings", []),
            tld = data.get("tld", []),
            cca2 = data.get("cca2"),
            ccn3 = data.get("ccn3"),
            cca3 = cca3,
            cioc = data.get("cioc"),
            independent = data.get("independent", False),
            status = data.get("status"),
            un_member = data.get("unMember", False),
            idd_root = data.get("idd", {}).get("root"),
            idd_suffixes = data.get("idd", {}).get("suffixes", []),
            region = data.get("region"),
            subregion = data.get("subregion"),
            latlng = data.get("latlng", []),
            landlocked = data.get("landlocked", False),
            area = data.get("area", 0.0),
            capital = data.get("capital", []),
            capital_info = data.get("capitalInfo", {}),
            population = data.get("population", 0),
            demonyms = data.get("demonyms", {}),
            gini = data.get("gini", {}),
            fifa = data.get("fifa"),
            timezones = data.get("timezones", []),
            start_of_week = data.get("startOfWeek"),
            car_signs = data.get("car", {}).get("signs", []),
            car_side = data.get("car", {}).get("side"),
            postal_code_format = data.get("postalCode", {}).get("format"),
            postal_code_regex = data.get("postalCode", {}).get("regex"),
            flag = data.get("flag"),
            flag_png = data.get("flags", {}).get("png"),
            flag_svg = data.get("flags", {}).get("svg"),
            flag_alt = data.get("flags", {}).get("alt"),
            coat_of_arms_png = data.get("coatOfArms", {}).get("png"),
            coat_of_arms_svg = data.get("coatOfArms", {}).get("svg"),
            maps_google = data.get("maps", {}).get("googleMaps"),
            maps_osm = data.get("maps", {}).get("openStreetMaps"),
        )

        # Add M2M fields
        for cont_name in data.get("continents", []):
            cont, _ = Continent.objects.get_or_create(name=cont_name)
            country.continents.add(cont)

        for b in data.get("borders", []):
            neighbor = Country.objects.filter(cca3=b).first()
            if neighbor:
                country.borders.add(neighbor)

        for code, name in data.get("languages", {}).items():
            lang, _ = Language.objects.get_or_create(code=code, defaults={"name": name})
            country.languages.add(lang)

        for code, info in data.get("currencies", {}).items():
            cur, _ = Currency.objects.get_or_create(code=code, defaults={"name": info.get("name"), "symbol": info.get("symbol")})
            country.currencies.add(cur)

        for lang_code, vals in data.get("translations", {}).items():
            Translation.objects.create(
                country=country,
                language_code=lang_code,
                official=vals.get("official"),
                common=vals.get("common"),
            )

        return Response({"success": "Country created successfully."}, status=status.HTTP_201_CREATED)
    

class CountryUpdateAPIView(APIView):
    @transaction.atomic
    def put(self, request, cca3):
        original_cca3 = cca3.upper()
        data = request.data
        new_cca3 = data.get("cca3", "").upper()

        try:
            country = Country.objects.get(cca3=original_cca3)
        except Country.DoesNotExist:
            return Response({"error": "Country not found."}, status=status.HTTP_404_NOT_FOUND)

        if new_cca3 != original_cca3:
            if Country.objects.filter(cca3=new_cca3).exclude(id=country.id).exists():
                return Response({"error": "A country with this new cca3 already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Update core fields
        country.name_common = data["name"]["common"]
        country.name_official = data["name"]["official"]
        country.native_names = data["name"].get("nativeName", {})
        country.alt_spellings = data.get("altSpellings", [])
        country.tld = data.get("tld", [])
        country.cca2 = data.get("cca2")
        country.ccn3 = data.get("ccn3")
        country.cca3 = data.get("cca3")
        country.cioc = data.get("cioc")
        country.independent = data.get("independent", False)
        country.status = data.get("status")
        country.un_member = data.get("unMember", False)
        country.idd_root = data.get("idd", {}).get("root")
        country.idd_suffixes = data.get("idd", {}).get("suffixes", [])
        country.region = data.get("region")
        country.subregion = data.get("subregion")
        country.latlng = data.get("latlng", [])
        country.landlocked = data.get("landlocked", False)
        country.area = data.get("area", 0.0)
        country.capital = data.get("capital", [])
        country.capital_info = data.get("capitalInfo", {})
        country.population = data.get("population", 0)
        country.demonyms = data.get("demonyms", {})
        country.gini = data.get("gini", {})
        country.fifa = data.get("fifa")
        country.timezones = data.get("timezones", [])
        country.start_of_week = data.get("startOfWeek")
        country.car_signs = data.get("car", {}).get("signs", [])
        country.car_side = data.get("car", {}).get("side")
        country.postal_code_format = data.get("postalCode", {}).get("format")
        country.postal_code_regex = data.get("postalCode", {}).get("regex")
        country.flag = data.get("flag")
        country.flag_png = data.get("flags", {}).get("png")
        country.flag_svg = data.get("flags", {}).get("svg")
        country.flag_alt = data.get("flags", {}).get("alt")
        country.coat_of_arms_png = data.get("coatOfArms", {}).get("png")
        country.coat_of_arms_svg = data.get("coatOfArms", {}).get("svg")
        country.maps_google = data.get("maps", {}).get("googleMaps")
        country.maps_osm = data.get("maps", {}).get("openStreetMaps")

        country.save()

        # Update ManyToMany relationships if provided
        if "continents" in data:
            country.continents.clear()
            for cont_name in data["continents"]:
                cont, _ = Continent.objects.get_or_create(name=cont_name)
                country.continents.add(cont)

        if "borders" in data:
            country.borders.clear()
            for border_cca3 in data["borders"]:
                neighbor = Country.objects.filter(cca3=border_cca3.upper()).first()
                if neighbor:
                    country.borders.add(neighbor)

        if "languages" in data:
            country.languages.clear()
            for code, name in data["languages"].items():
                lang, _ = Language.objects.get_or_create(code=code, defaults={"name": name})
                country.languages.add(lang)

        if "currencies" in data:
            country.currencies.clear()
            for code, info in data["currencies"].items():
                cur, _ = Currency.objects.get_or_create(
                    code=code,
                    defaults={"name": info.get("name"), "symbol": info.get("symbol")},
                )
                country.currencies.add(cur)

        if "translations" in data:
            country.translations.all().delete()
            for lang_code, vals in data["translations"].items():
                Translation.objects.create(
                    country=country,
                    language_code=lang_code,
                    official=vals.get("official"),
                    common=vals.get("common"),
                )

        return Response({"success": f"Country '{country.name_common}' updated successfully."})
    

class CountryDeleteAPIView(APIView):
    def delete(self, request, cca3):
        cca3 = cca3.upper()  # Ensure consistent formatting
        country = get_object_or_404(Country, cca3=cca3)

        country.delete()
        return Response(
            {"message": f"Country with CCA3 '{cca3}' deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
    

class RegionalCountriesAPIView(APIView):
    def get(self, request, cca3):
        cca3 = cca3.upper()
        country = get_object_or_404(Country, cca3=cca3)

        region = country.region
        if not region:
            return Response(
                {"error": f"Region not set for country '{cca3}'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # All other countries in the same region
        same_region_countries = Country.objects.filter(region=region).exclude(cca3=cca3)
        names = list(same_region_countries.values_list('name_common', flat=True))

        return Response(names, status=status.HTTP_200_OK)
    

class CountriesByLanguageAPIView(APIView):
    def get(self, request, lang_code):
        # Normalize language code
        lang_code = lang_code.lower()

        # Ensure the language exists
        language = get_object_or_404(Language, code=lang_code)

        # All countries that have this language
        countries = Country.objects.filter(languages=language)
        names = list(countries.values_list('name_common', flat=True))

        if not names:
            return Response(
                {"message": f"No countries found for language '{lang_code}'."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(names, status=status.HTTP_200_OK)
