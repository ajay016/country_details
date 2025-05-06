from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from country_info.models import *
from .serializers import CountryNameSerializer



class CountryListAPIView(APIView):
    def get(self, request):
        names = list(Country.objects.values_list('name_common', flat=True))
        return Response(names, status=status.HTTP_200_OK)
