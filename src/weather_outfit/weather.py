import requests


url = "https://api.open-meteo.com/v1/forecast"
    
    

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 36.9741,
        "longitude": -122.0308,
        "current": (
            "temperature_2m,"
            "apparent_temperature,"
            "precipitation,"
            "wind_speed_10m,"
            "weather_code,"
            "wind_direction_10m"
        ),
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()