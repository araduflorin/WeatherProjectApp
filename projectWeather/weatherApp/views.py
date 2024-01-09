import requests
from django.shortcuts import render

from projectWeather.secret_key import value_secret_key
from .models import City
from .forms import CityForm

def index(request):
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + value_secret_key
    url = 'https://api.openweathermap.org/data/3.0/onecall?lat=39.099724&lon=94.578331&units=metric&appid=' + value_secret_key

    # city = 'Barcelona'
    cities = City.objects.all()  # return all the cities in the database

    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        form.save()  # will validate and save if validate

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()  # request the API data and convert the JSON to Python data types
    # print(city_weather)
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)  # add the data for the current city into our list

    context = {'weather_data': weather_data, 'form' : form}
    return render(request, 'weatherApp/index.html',context)  # returns the index.html template
