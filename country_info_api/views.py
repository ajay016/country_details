from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
