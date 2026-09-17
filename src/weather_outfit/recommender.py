def calculate_match(need, capability):
    difference = abs(need - capability)
    return 1 - difference


def calculate_protection_match(need, capability):
    if need == 0:
        return 1.0

    if capability >= need:
        return 1.0

    return capability / need


def get_weights(environment):
    weights = {
        "warmth": 1.0,
        "rain": environment["rain_protection_need"],
        "wind": environment["wind_protection_need"],
        "breathability": 1.0,
    }

    return weights


def calculate_context_penalty(item, environment):
    penalty = 0.0

    if (
        item["primary_purpose"] == "rain"
        and environment["rain_protection_need"] == 0
    ):
        penalty += 0.15

    return penalty


def score_item(item, environment):
    warmth_score = calculate_match(
        environment["warmth_need"],
        item["warmth"]
    )

    rain_score = calculate_protection_match(
        environment["rain_protection_need"],
        item["rain_protection"]
    )

    wind_score = calculate_protection_match(
        environment["wind_protection_need"],
        item["wind_protection"]
    )

    breathability_score = calculate_match(
        environment["breathability_need"],
        item["breathability"]
    )

    weights = get_weights(environment)

    weighted_total = (
        warmth_score * weights["warmth"]
        + rain_score * weights["rain"]
        + wind_score * weights["wind"]
        + breathability_score * weights["breathability"]
    )

    weight_sum = (
        weights["warmth"]
        + weights["rain"]
        + weights["wind"]
        + weights["breathability"]
    )

    total_score = weighted_total / weight_sum

    context_penalty = calculate_context_penalty(
        item,
        environment
    )

    total_score -= context_penalty

    return max(total_score, 0.0)


def rank_items(items, environment):
    scored_items = []

    for item in items:
        score = score_item(item, environment)

        scored_items.append({
            "name": item["name"],
            "score": score,
        })

    scored_items.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return scored_items


tshirt = {
    "name": "T-shirt",
    "primary_purpose": "general",
    "warmth": 0.2,
    "rain_protection": 0.0,
    "wind_protection": 0.1,
    "breathability": 0.9,
}

hoodie = {
    "name": "Hoodie",
    "primary_purpose": "warmth",
    "warmth": 0.8,
    "rain_protection": 0.2,
    "wind_protection": 0.5,
    "breathability": 0.3,
}

rain_shell = {
    "name": "Rain Jacket",
    "primary_purpose": "rain",
    "warmth": 0.3,
    "rain_protection": 1.0,
    "wind_protection": 0.9,
    "breathability": 0.5,
}

light_jacket = {
    "name": "Light jacket",
    "primary_purpose": "general",
    "warmth": 0.6,
    "rain_protection": 0.4,
    "wind_protection": 0.7,
    "breathability": 0.5,
}


clothing_items = [
    tshirt,
    hoodie,
    rain_shell,
    light_jacket,
]