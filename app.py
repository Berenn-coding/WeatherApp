
import pygame
import requests
import random
import math

WIDTH = 800
HEIGHT = 500

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

    except (requests.RequestException, ValueError, KeyError) as error:
        print("Weather error:", error)
        return None


def get_weather_type(code):
    if code == 0:
        return "sunny"
    elif code in [1, 2, 3]:
        return "cloudy"
    elif code in [45, 48]:
        return "foggy"
    elif code in [51, 53, 55, 56, 57, 61, 63, 65,
                  66, 67, 80, 81, 82]:
        return "rainy"
    elif code in [71, 73, 75, 77, 85, 86]:
        return "snowy"
    elif code in [95, 96, 99]:
        return "stormy"
    else:
        return "cloudy"


def draw_cloud(screen, x, y):
    color = (240, 240, 245)

    pygame.draw.circle(screen, color, (int(x), int(y)), 30)
    pygame.draw.circle(screen, color, (int(x + 35), int(y - 15)), 40)
    pygame.draw.circle(screen, color, (int(x + 75), int(y)), 30)
    pygame.draw.rect(screen, color, (int(x), int(y), 75, 25))


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
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

raindrops = []

for i in range(100):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    speed = random.randint(5, 12)
    raindrops.append([x, y, speed])

snowflakes = []

for i in range(80):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    speed = random.randint(1, 4)
    snowflakes.append([x, y, speed])

cloud_x = 100
sun_time = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if weather_type == "sunny":
        screen.fill((90, 180, 255))

        sun_time += 0.04
        sun_radius = 60 + int(5 * math.sin(sun_time))

        pygame.draw.circle(
            screen,
            (255, 220, 50),
            (650, 110),
            sun_radius
        )

    elif weather_type == "rainy":
        screen.fill((50, 70, 100))

        for drop in raindrops:
            pygame.draw.line(
                screen,
                (150, 200, 255),
                (drop[0], drop[1]),
                (drop[0], drop[1] + 15),
                2
            )

            drop[1] += drop[2]

            if drop[1] > HEIGHT:
                drop[1] = 0
                drop[0] = random.randint(0, WIDTH)

    elif weather_type == "snowy":
        screen.fill((180, 210, 230))

        for flake in snowflakes:
            pygame.draw.circle(
                screen,
                (255, 255, 255),
                (flake[0], flake[1]),
                4
            )

            flake[1] += flake[2]

            if flake[1] > HEIGHT:
                flake[1] = 0
                flake[0] = random.randint(0, WIDTH)

    elif weather_type == "cloudy":
        screen.fill((110, 160, 200))

        draw_cloud(screen, cloud_x, 100)
        draw_cloud(screen, cloud_x + 300, 180)

        cloud_x += 0.5

        if cloud_x > WIDTH:
            cloud_x = -400

    elif weather_type == "stormy":
        screen.fill((40, 45, 75))

        for drop in raindrops:
            pygame.draw.line(
                screen,
                (150, 180, 255),
                (drop[0], drop[1]),
                (drop[0], drop[1] + 20),
                2
            )

            drop[1] += drop[2]

            if drop[1] > HEIGHT:
                drop[1] = 0

    else:
        screen.fill((130, 150, 170))

    city_text = font.render("Cambridge", True, (255, 255, 255))
    screen.blit(city_text, (280, 140))

    if temperature is not None:
        temp_text = font.render(
            f"{temperature} °C",
            True,
            (255, 255, 255)
        )
    else:
        temp_text = font.render(
            "Weather unavailable",
            True,
            (255, 255, 255)
        )

    screen.blit(temp_text, (280, 220))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
