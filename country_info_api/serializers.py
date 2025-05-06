from rest_framework import serializers
from country_info.models import *


class CountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name_common']