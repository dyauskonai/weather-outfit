def calculate_match(need,capability):
    difference = abs(need - capability)
    return 1 - difference


hoodie = {
    "name": "Hoodie",
    "warmth": 0.8,
    "rain_protection": 0.2,
    "wind_protection": 0.5,
    "breathability": 0.3,
}
environment = {
    "warmth_need": 0.6,
    "rain_protection_need": 0.2,
    "wind_protection_need": 0.5,
    "breathability_need": 0.4,
}

def score_item(item, environment):
    warmth_score = calculate_match(
        environment["warmth_need"],
        item["warmth"]
    )

    rain_score = calculate_match(
        environment["rain_protection_need"],
        item["rain_protection"]
    )

    wind_score = calculate_match(
        environment["wind_protection_need"],
        item["wind_protection"]
    )

    breathability_score = calculate_match(
        environment["breathability_need"],
        item["breathability"]
    )

    total_score = (
        warmth_score
        + rain_score
        + wind_score
        + breathability_score
    ) / 4

    return total_score



print(round(score_item(hoodie, environment),3))