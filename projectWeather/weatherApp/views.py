import math
from datetime import datetime

import requests
from django.shortcuts import render

from projectWeather.secret_key import value_secret_key
from .models import City
from .forms import CityForm


# def index(request):
#     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + value_secret_key
#     # url = 'https://api.openweathermap.org/data/3.0/onecall?lat=39.099724&lon=94.578331&units=metric&appid=' + value_secret_key
#
#     # city = 'Barcelona'
#     cities = City.objects.all()  # return all the cities in the database
#
#     if request.method == 'POST':  # only true if form is submitted
#         form = CityForm(request.POST)  # add actual request data to form for processing
#         form.save()  # will validate and save if validate
#
#     form = CityForm()
#
#     weather_data = []
#
#     for city in cities:
#         city_weather = requests.get(url.format(city)).json()  # request the API data and convert the JSON to Python data types
#     # print(city_weather)
#         weather = {
#             'city': city,
#             'temperature': city_weather['main']['temp'],
#             'description': city_weather['weather'][0]['description'] ,
#             'icon': city_weather['weather'][0]['icon']
#         }
#         weather_data.append(weather)  # add the data for the current city into our list
#
#     context = {'weather_data': weather_data, 'form' : form}
#     return render(request, 'weatherApp/index.html',context)  # returns the index.html template

######################### Another variant ################

# the index() will handle all the app's logic
def index(request):
    # if there are no errors the code inside try will execute
    try:
        # checking if the method is POST
        if request.method == 'POST':
            API_KEY = value_secret_key
            # getting the city name from the form input
            city_name = request.POST.get('city')
            # the url for current weather, takes city_name and API_KEY
            url_current = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            # converting the request response to json
            response_current = requests.get(url_current).json()
            # getting the current time
            current_time = datetime.now()
            # formatting the time using directives, it will take this format Day, Month Date Year, Current Time
            # formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            formatted_time = current_time.strftime("%H:%M  %b %d")
            # bundling the weather information in one dictionary
            city_weather_update = {
                'city': city_name,
                'description': response_current['weather'][0]['description'],
                'icon': response_current['weather'][0]['icon'],
                'temperature': response_current['main']['temp'],
                'feels_like': response_current['main']['feels_like'],
                'country_code': response_current['sys']['country'],
                'wind': '' + str(response_current['wind']['speed']) + ' m/s',
                'humidity': '' + str(response_current['main']['humidity']) + '%',
                'pressure': '' + str(response_current['main']['pressure']) + ' hPa',
                'snow': '' + str(response_current['snow']['1h']) ,
                # 'precipitation': 'Precipitation:' + str(response['main']['precipitation']) + '%',
                'time': formatted_time
            }
            # print(type(city_weather_update.temperature))
        # if the request method is GET empty the dictionary
        else:
            city_weather_update = {}
        context = {'city_weather_update': city_weather_update}
        return render(request, 'weatherApp/home.html', context)
    # if there is an error the 404 page will be rendered
    # the except will catch all the errors
    except:
        return render(request, 'weatherApp/404.html')


# from django.shortcuts import render

# def weather_widget_view(request):
#     if request.method == 'POST':
#         city = request.POST.get('city')  # Retrieve city from form submission
#
#         # Generate widget parameters
#         widget_params = [
#             {
#                 'id': 15,
#                 'cityid': 2643743, #city,  # Replace hardcoded city ID with actual input
#                 'appid': '4c1262c471ca84404de85d2fd0bc73ff',
#                 'units': 'metric',
#                 'containerid': 'openweathermap-widget-15',
#             },
#         ]
#
#         context = {
#             'widget_params': widget_params,
#         }
#         return render(request, 'weatherApp/weather_widget.html', context)
#     else:
#         return render(request, 'weatherApp/index1.html')

