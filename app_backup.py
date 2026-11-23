
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


def get_weather_type(code):
    if code == 0:
        return "sunny"
    elif code in [1, 2, 3]:
        return "cloudy"
    elif code in [51, 53, 55, 56, 57, 61, 63, 65,
                  66, 67, 80, 81, 82]:
        return "rainy"
    elif code in [71, 73, 75, 77, 85, 86]:
        return "snowy"
    elif code in [95, 96, 99]:
        return "stormy"
    else:
        return "cloudy"


pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("My Weather App")

font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()

weather = get_weather()

if weather is not None:
    temperature = weather["temperature_2m"]
    weather_type = get_weather_type(weather["weather_code"])
else:
    temperature = None
    weather_type = "unavailable"

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if weather_type == "sunny":
        screen.fill((90, 180, 255))
        pygame.draw.circle(screen, (255, 220, 50), (650, 110), 60)

    elif weather_type == "rainy":
        screen.fill((50, 70, 100))

    elif weather_type == "snowy":
        screen.fill((180, 210, 230))

    elif weather_type == "stormy":
        screen.fill((40, 45, 75))

    else:
        screen.fill((110, 130, 150))

    city_text = font.render("Cambridge", True, (255, 255, 255))
    screen.blit(city_text, (280, 140))

    if temperature is not None:
        temp_text = font.render(f"{temperature} °C", True, (255, 255, 255))
    else:
        temp_text = font.render("Weather unavailable", True, (255, 255, 255))

    screen.blit(temp_text, (280, 220))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
