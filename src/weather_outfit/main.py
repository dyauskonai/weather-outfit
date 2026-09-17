import requests
from utils import get_wind_direction, weather_codes
from weather import get_weather
from comfort import build_environment_profile
from recommender import rank_items_by_category
from wardrobe import load_wardrobe, manage_wardrobe


def main():
    print("\nWeather Outfit")

    try:
        clothing_items = load_wardrobe()
    except (OSError, ValueError) as error:
        print(f"Could not load your wardrobe: {error}")
        return

    clothing_items = manage_wardrobe(clothing_items)

    if not clothing_items:
        print("Your wardrobe is empty, so there is nothing to recommend yet.\n")
        return

    try:
        data = get_weather()
    except requests.exceptions.RequestException as error:
        print("Could not retrieve the weather.", error)
        return

    temperature = data["current"]["temperature_2m"]
    apparent_temperature = data["current"]["apparent_temperature"]
    precipitation = data["current"]["precipitation"]
    wind_speed = data["current"]["wind_speed_10m"]
    wind_direction = data["current"]["wind_direction_10m"]
    wind_compass = get_wind_direction(wind_direction)
    weather_code = data["current"]["weather_code"]
    condition = weather_codes.get(weather_code, "Unknown weather condition")

    environment = build_environment_profile(
        apparent_temperature,
        wind_speed,
        precipitation,
    )
    ranked_by_category = rank_items_by_category(clothing_items, environment)

    print(f"\nCurrent temperature in Santa Cruz: {temperature}°F")
    print(f"Feels like: {int(apparent_temperature)}°F")
    print(f"Precipitation: {precipitation:.2f} inches")
    print(f"Wind Conditions: {wind_speed} mph {wind_compass}")
    print(condition)

    print("\nRecommended clothing:")

    for category, ranked_items in ranked_by_category.items():
        print(f"\n{category.title()}:")

        for item in ranked_items:
            print(f'{item["name"]}: {item["score"] * 100:.1f}%')

    print()


if __name__ == "__main__":
    main()
