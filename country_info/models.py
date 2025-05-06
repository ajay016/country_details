from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Language(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Translation(models.Model):
    country = models.ForeignKey("Country", on_delete=models.CASCADE, related_name="translations")
    language_code = models.CharField(max_length=10)
    official = models.CharField(max_length=200)
    common = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.language_code} - {self.common}"

class Continent(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Country(models.Model):
    name_common = models.CharField(max_length=100)
    name_official = models.CharField(max_length=200)
    native_names = models.JSONField(null=True, blank=True)

    tld = models.JSONField()
    cca2 = models.CharField(max_length=2, null=True, blank=True)
    ccn3 = models.CharField(max_length=3, null=True, blank=True)
    cca3 = models.CharField(max_length=3, null=True, blank=True)
    cioc = models.CharField(max_length=3, null=True, blank=True)

    independent = models.BooleanField(default=False)
    status = models.CharField(max_length=50)
    un_member = models.BooleanField(default=False)

    currencies = models.ManyToManyField(Currency)
    idd_root = models.CharField(max_length=5, null=True, blank=True)
    idd_suffixes = models.JSONField(null=True, blank=True)

    capital = models.JSONField()
    alt_spellings = models.JSONField()

    region = models.CharField(max_length=80, null=True, blank=True)
    subregion = models.CharField(max_length=50, null=True, blank=True)

    languages = models.ManyToManyField(Language)
    latlng = models.JSONField()
    landlocked = models.BooleanField(default=False)
    borders = models.ManyToManyField("self", symmetrical=True, blank=True)
    area = models.FloatField(null=True, blank=True)

    demonyms = models.JSONField(null=True, blank=True)
    population = models.BigIntegerField()
    gini = models.JSONField(null=True, blank=True)
    fifa = models.CharField(max_length=3, null=True, blank=True)

    car_signs = models.JSONField(null=True, blank=True)
    car_side = models.CharField(max_length=50, null=True, blank=True)

    timezones = models.JSONField()
    continents = models.ManyToManyField(Continent)

    flag = models.CharField(max_length=10, null=True, blank=True)
    flag_png = models.URLField(null=True, blank=True)
    flag_svg = models.URLField(null=True, blank=True)
    flag_alt = models.CharField(max_length=255, null=True, blank=True)
    coat_of_arms_png = models.URLField(null=True, blank=True)
    coat_of_arms_svg = models.URLField(null=True, blank=True)

    maps_google = models.URLField(null=True, blank=True)
    maps_osm = models.URLField(null=True, blank=True)

    start_of_week = models.CharField(max_length=10)
    capital_info = models.JSONField(null=True, blank=True)
    postal_code_format = models.CharField(max_length=100, null=True, blank=True)
    postal_code_regex = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name_common