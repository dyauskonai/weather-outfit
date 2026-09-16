import requests
from utils import get_wind_direction, weather_codes
from weather import get_weather
print("\n")
try:
    data = get_weather()

    temperature = data["current"]["temperature_2m"]
    apparent_temperature = data["current"]["apparent_temperature"]
    precipitation = data["current"]["precipitation"]
    wind_speed = data["current"]["wind_speed_10m"]
    wind_direction = data["current"]["wind_direction_10m"]
    wind_compass = get_wind_direction(wind_direction)
    weather_code = data["current"]["weather_code"]
    condition = weather_codes.get(weather_code, "Unknown weather condition")
    
    

    print(f"Current temperature in Santa Cruz: {temperature}°F")
    print(f"Feels like: {int(apparent_temperature)}°F")
    print(f"Precipitation: {precipitation:.2f} inches")
    print(f"Wind Conditions: {wind_speed} mph from {wind_compass}")
    print(f"Condition: {condition}")


    print("\n")
except requests.exceptions.RequestException as e:
    print("Request failed." , e)
    print("\n")
