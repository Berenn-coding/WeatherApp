

import pygame
import requests


def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 52.2053,
        "longitude": 0.1218,
        "current": "temperature_2m,weather_code"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["current"]

    except (requests.RequestException, ValueError, KeyError):
        return None


def get_weather_type(code, temperature):
    if code == 0:
        weather = "sunny"
    elif code in [1, 2, 3]:
        weather = "cloudy"
    elif code in [51, 53, 55, 56, 57, 61, 63, 65,
                  66, 67, 80, 81, 82]:
        weather = "rainy"
    elif code in [71, 73, 75, 77, 85, 86]:
        weather = "snowy"
    elif code in [95, 96, 99]:
        weather = "stormy"
    else:
        weather = "cloudy"

    if temperature <= 4:
        feeling = "very cold"
    elif temperature <= 10:
        feeling = "cold"
    elif temperature <= 17:
        feeling = "cool"
    elif temperature <= 24:
        feeling = "warm"
    else:
        feeling = "hot"

    # Custom display rule for very cold weather
    if temperature <= 4 and weather == "sunny":
        weather = "cloudy"

    return weather, feeling


pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("My Weather App")

font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()

weather = get_weather()

if weather is not None:
    temperature = weather["temperature_2m"]

    weather_type, temperature_feeling = get_weather_type(
        weather["weather_code"], temperature
    )
else:
    temperature = None
    weather_type = "unavailable"
    temperature_feeling = "unavailable"


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if weather_type == "sunny":
        screen.fill((90, 180, 255))
        pygame.draw.circle(
            screen, (255, 220, 50), (650, 110), 60
        )

    elif weather_type == "rainy":
        screen.fill((50, 70, 100))

    elif weather_type == "snowy":
        screen.fill((180, 210, 230))

    elif weather_type == "stormy":
        screen.fill((40, 45, 75))

    else:
        screen.fill((110, 130, 150))

    city_text = font.render(
        "Cambridge", True, (255, 255, 255)
    )
    screen.blit(city_text, (280, 140))

    if temperature is not None:
        temp_text = font.render(
            f"{temperature} °C", True, (255, 255, 255)
        )

        feeling_text = font.render(
            temperature_feeling.title(),
            True,
            (255, 255, 255)
        )

        weather_text = font.render(
            weather_type.title(),
            True,
            (255, 255, 255)
        )

        screen.blit(temp_text, (280, 220))
        screen.blit(feeling_text, (280, 290))
        screen.blit(weather_text, (280, 360))

    else:
        error_text = font.render(
            "Weather unavailable",
            True,
            (255, 255, 255)
        )
        screen.blit(error_text, (200, 220))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
