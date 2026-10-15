import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 35.94,
    "longitude": -77.79,
    "current": "temperature_2m,wind_speed_10m",
    "temperature_unit": "fahrenheit",
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()
data = response.json()

print("Current conditions:")
print(f"  Temperature: {data['current']['temperature_2m']} F")
print(f"  Wind speed:  {data['current']['wind_speed_10m']} km/h")
