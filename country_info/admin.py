from django.contrib import admin
from .models import Currency, Language, Translation, Continent, Country


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "symbol")
    search_fields = ("code", "name")


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ("country", "language_code", "common", "official")
    search_fields = ("language_code", "common", "official")
    list_filter = ("language_code",)


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name_common", "cca2", "cca3", "region", "subregion", "population")
    search_fields = ("name_common", "cca2", "cca3")
    list_filter = ("region", "subregion", "un_member", "landlocked")
    filter_horizontal = ("currencies", "languages", "borders", "continents")
    readonly_fields = ("flag",)