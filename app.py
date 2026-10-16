import requests

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


def get_current_weather(latitude, longitude):
    """Return current temperature (F) and wind speed (km/h) for a location."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "temperature_unit": "fahrenheit",
    }
    response = requests.get(FORECAST_URL, params=params, timeout=10)
    response.raise_for_status()
    current = response.json()["current"]
    return {
        "temperature": current["temperature_2m"],
        "wind_speed": current["wind_speed_10m"],
    }
def print_weather(label, weather):
    print(f"{label}:")
    print(f"  Temperature: {weather['temperature']} F")
    print(f"  Wind speed:  {weather['wind_speed']} km/h")


def main():
    weather = get_current_weather(35.94, -77.79)
    weather2 = get_current_weather(35.896, -77.854)

    print_weather("Current conditions", weather)
    print_weather("Current conditions (second location)", weather2)


if __name__ == "__main__":
    main()