import requests
from django.shortcuts import render

from .city_controller import get_all_city_names_starting_with_v
from .weather_config import weather_api_key


def index(request):
    cities = get_all_city_names_starting_with_v()
    context = {'cities': cities}
    return render(request, 'weatherapp/index.html', context)


def info(request, info_id):
    city_name = get_all_city_names_starting_with_v()[info_id]
    key = weather_api_key  # get key from here -> https://openweathermap.org/current
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={key}'

    r = requests.get(url).json()
    city_weather = {
        'name': city_name,
        'temperature': r['main']['temp'],
        'humidity': r['main']['humidity'],
        'wind': r['wind']['speed'],
        'icon': r['weather'][0]['icon'],
    }

    return render(request, "weatherapp/info.html", {
        "city": city_weather
    })
