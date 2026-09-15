import requests

print("\n")
try:
    url = "https://api.open-meteo.com/v1/forecast"
    
    symbolInput = input("Farenheit or Celsius?").strip().title()
    if symbolInput == "Farenheit":
        temperature_unit = "fahrenheit"
        symbol = "°F"
    elif symbolInput == "Celsius":
        temperature_unit = "celsius"
        symbol = "°C"
    else:
        print("Invalid input. Please enter 'Farenheit' or 'Celsius'.")
        exit()
   
        
    
    
    

    params = {
        "latitude": 36.9741,
        "longitude": -122.0308,
        "current": "temperature_2m,apparent_temperature",
        "temperature_unit": temperature_unit,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    temperature = data["current"]["temperature_2m"]
    apparent_temperature = data["current"]["apparent_temperature"]

    print(f"Current temperature in Santa Cruz: {temperature}{symbol}")
    print(f"Feels like: {apparent_temperature}{symbol}")

    print("\n")
except requests.exceptions.RequestException as e:
    print("Request failed." , e)
    print("\n")
