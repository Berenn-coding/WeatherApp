# 🌤️ WeatherApp

A simple desktop weather application developed using **Python**, **Pygame**, and the **Open-Meteo API**.

WeatherApp retrieves real-time weather data for Cambridge, United Kingdom, and displays the current temperature and weather conditions through a graphical interface.

## ✨ Features

- 🌡️ Displays the current temperature in Celsius
- ☀️ Supports sunny, cloudy, rainy, snowy, and stormy weather conditions
- 🥶 Classifies temperatures as Very Cold, Cold, Cool, Warm, or Hot
- 🎨 Changes the background colour based on weather conditions
- 🌍 Retrieves live weather data using the Open-Meteo API
- 🖥️ Provides a graphical desktop interface using Pygame

## 🛠️ Technologies Used

- **Python** – Main programming language
- **Pygame** – Graphical user interface
- **Requests** – API requests
- **Open-Meteo API** – Weather information
- **Git & GitHub** – Version control

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Berenn-coding/WeatherApp.git
cd WeatherApp
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the required libraries

```bash
python -m pip install pygame-ce requests
```

### 4. Run the application

```bash
python app.py
```

A Pygame window will open and display the current weather information.

## 🌦️ How It Works

1. The application sends an HTTP request to the Open-Meteo API.
2. The API returns weather information in JSON format.
3. Python processes the temperature and weather code.
4. The application classifies the weather and temperature.
5. Pygame displays the results in a graphical window.

## 🌡️ Temperature Classification

| Temperature | Description |
|---|---|
| 4°C and below | Very Cold |
| Above 4°C to 10°C | Cold |
| Above 10°C to 17°C | Cool |
| Above 17°C to 24°C | Warm |
| Above 24°C | Hot |

**Note:** The application uses a custom display rule that shows cloudy conditions when the temperature is 4°C or below and the API reports sunny weather.

## 📍 Current Location

**Cambridge, United Kingdom**

Future versions may support searching for different cities.

## 🔮 Future Improvements

- Add a city search feature
- Display hourly and weekly weather forecasts
- Introduce animated weather effects
- Improve the graphical interface
- Add automatic weather updates
- Package the application for easier installation

## 📚 About This Project

WeatherApp is a personal Python project created to practise programming, API integration, conditional statements, functions, graphical user interfaces, and version control.

## 👩‍💻 Developer

**Beren**

GitHub: [@Berenn-coding](https://github.com/Berenn-coding)
