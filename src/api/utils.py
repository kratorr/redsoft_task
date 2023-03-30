import requests
import datetime

from django.conf import settings


def get_weather(city: str, date):
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = settings.OPENWEATHER_KEY
    dt_object = datetime.datetime(date.year, date.month, date.day)
    headers = {'content-type': 'application/json'}
    params = {
        "q": city,
        "appid": api_key,
        "dt": int(dt_object.timestamp())
    }
    response = requests.get(api_url, params=params, headers=headers)

    if response.status_code == 200:
        response = response.json()
    else:
        response = 'Error to fetch weather'

    return response
