from django.shortcuts import render, redirect
import json
from django.http import HttpResponse

import requests

SLUG_URL = "https://api.covid19api.com/countries"
COUNTRY_INFO_URL = "https://api.covid19api.com/dayone/country/"

countrySlugs = dict()


# Create your views here.

def hi(request):
    response = requests.get(SLUG_URL)
    data = response.text
    parsed = json.loads(data)
    for country in parsed:
        countrySlugs[country["Country"]] = country["Slug"]

    return render(request, 'DEMOAPP/index.html')


def get_country(request):
    countryName = request.GET.get('searchedCountry')
    if countryName not in countrySlugs.keys():
        return redirect('/')

    countrySearchSlug = countrySlugs[countryName]

    response = requests.get(COUNTRY_INFO_URL + countrySearchSlug)

    data = response.text
    parsed = json.loads(data)

    countryStats = list()
    for stat in parsed:
        if stat["Province"] == "":
            stat["Date"] = stat["Date"][0:10]
            countryStats.append(stat)
    return render(request, 'DEMOAPP/countrystats.html', {"countryStats": countryStats})
