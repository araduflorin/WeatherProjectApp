import requests
from django.shortcuts import render

from projectWeather.projectWeather.secret_key import value_secret_key


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + value_secret_key

    city = 'Barcelona'

    city_weather = requests.get(url.format(city)).json()  # request the API data and convert the JSON to Python data types
    print(city_weather)
    return render(request, 'weatherApp/index.html')  # returns the index.html template
