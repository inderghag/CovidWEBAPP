from django.db import models


# Create your models here.
class Country(models.Model):
    Country = models.CharField(max_length=100)
    CountryCode = models.CharField(max_length=10)
    City = models.CharField(max_length=100)
    CityCode = models.CharField(max_length=100)
    Lat = models.IntegerField()
    Lon = models.IntegerField()
    Confirmed = models.IntegerField()
    Deaths = models.IntegerField()
    Recovered = models.IntegerField()
    Active = models.IntegerField()
    Date = models.DateField()
