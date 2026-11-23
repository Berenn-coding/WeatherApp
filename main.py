import requests 
import pygame


def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 52.2053,
        "longitude": 0.1218,
        "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        current = data["current"]

        print("CAMBRIDGE WEATHER")
        print(" ")
        print("Temperature: ", current["temperature_2m"], "°C" )
        print("Humidity: ", current["relative_humidity_2m"], "%")
        print("Wind Speed: ", current["wind_speed_10m"], "km/h")
        print("Weather Code: ", current["weather_code"])

    except requests.RequestException as error:
          print("Could not get weather: ", error)

    get_weather()