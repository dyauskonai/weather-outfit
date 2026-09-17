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

    if (item["primary_purpose"] == "rain" and environment["rain_protection_need"] == 0):
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

    context_penalty = calculate_context_penalty(item,environment)

    total_score -= context_penalty

    return max(total_score, 0.0)


def rank_items(items, environment):
    scored_items = []

    for item in items:
        score = score_item(item, environment)

        scored_items.append({
            "name": item["name"],
            "category": item["category"],
            "score": score,
        })

    scored_items.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return scored_items


def rank_items_by_category(items, environment):
    items_by_category = {}

    for item in items:
        category = item["category"]
        items_by_category.setdefault(category, []).append(item)

    ranked_by_category = {}

    for category, category_items in items_by_category.items():
        ranked_by_category[category] = rank_items(category_items, environment)

    return ranked_by_category
