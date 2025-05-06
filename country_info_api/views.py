from rest_framework.views import APIView
from rest_framework.response import Response
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