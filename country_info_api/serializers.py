from rest_framework import serializers
from country_info.models import *


class CountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name_common']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["symbol", "name"]

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ["code", "name"]

class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ["language_code", "official", "common"]

class CountrySerializer(serializers.ModelSerializer):
    currencies = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    translations = serializers.SerializerMethodField()
    borders = serializers.SerializerMethodField()
    continents = serializers.SlugRelatedField(many=True, slug_field="name", read_only=True)

    name = serializers.SerializerMethodField()
    idd = serializers.SerializerMethodField()
    maps = serializers.SerializerMethodField()
    car = serializers.SerializerMethodField()
    flags = serializers.SerializerMethodField()
    coatOfArms = serializers.SerializerMethodField()
    postalCode = serializers.SerializerMethodField()

    class Meta:
        model = Country
        exclude = [
            'name_common', 'name_official', 'native_names', 'idd_root', 'idd_suffixes', 'car_signs', 'car_side', 'flag_png',
            'flag_svg', 'flag_alt', 'coat_of_arms_png', 'coat_of_arms_svg', 'maps_google', 'maps_osm', 'postal_code_format', 'postal_code_regex'
        ]

    def get_name(self, obj):
        return {
            "common": obj.name_common,
            "official": obj.name_official,
            "nativeName": obj.native_names,
        }

    def get_idd(self, obj):
        return {
            "root": obj.idd_root,
            "suffixes": obj.idd_suffixes,
        } 

    def get_maps(self, obj):
        return {
            "googleMaps": obj.maps_google,
            "openStreetMaps": obj.maps_osm
        }

    def get_car(self, obj):
        return {
            "signs": obj.car_signs,
            "side": obj.car_side
        }

    def get_flags(self, obj):
        return {
            "png": obj.flag_png,
            "svg": obj.flag_svg,
            "alt": obj.flag_alt
        }

    def get_coatOfArms(self, obj):
        return {
            "png": obj.coat_of_arms_png,
            "svg": obj.coat_of_arms_svg,
        }


    def get_currencies(self, obj):
        return {
            currency.code: {
                "symbol": currency.symbol,
                "name": currency.name
            } for currency in obj.currencies.all()
        }

    def get_postalCode(self, obj):
        return {
            "format": obj.postal_code_format,
            "regex": obj.postal_code_regex
        }

    def get_languages(self, obj):
        return {language.code: language.name for language in obj.languages.all()}

    def get_translations(self, obj):
        result = {}
        for translation in obj.translations.all():
            result[translation.language_code] = {
                "official": translation.official,
                "common": translation.common
            }
        return result

    def get_borders(self, obj):
        return [border.cca3 for border in obj.borders.all()]