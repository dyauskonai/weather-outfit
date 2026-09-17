import json
from pathlib import Path
from uuid import uuid4


WARDROBE_PATH = Path(__file__).resolve().parents[2] / "data" / "wardrobe.json"

CATEGORY_CHOICES = {
    "Top": "top",
    "Outerwear": "outerwear",
    "Bottom": "bottom",
    "Footwear": "footwear",
}

PURPOSE_CHOICES = {
    "General use": "general",
    "Warmth": "warmth",
    "Rain protection": "rain",
}

ATTRIBUTE_LEVELS = {
    "None": 0.0,
    "Low": 0.25,
    "Medium": 0.5,
    "High": 0.75,
    "Very high": 1.0,
}

WARDROBE_ACTIONS = {
    "Add an item": "add",
    "Remove an item": "remove",
    "Continue to recommendations": "continue",
}


def ask_for_name():
    while True:
        name = input("Item name: ").strip()

        if name:
            return name

        print("Please enter a name for the item.")


def ask_for_choice(question, choices):
    choice_labels = list(choices.keys())

    while True:
        print(f"\n{question}")

        for number, label in enumerate(choice_labels, start=1):
            print(f"{number}. {label}")

        answer = input("Choose a number: ").strip()

        if answer.isdigit():
            selected_number = int(answer)

            if 1 <= selected_number <= len(choice_labels):
                selected_label = choice_labels[selected_number - 1]
                return choices[selected_label]

        print("Please choose one of the listed numbers.")


def create_clothing_item():
    print("\nAdd a clothing item")

    name = ask_for_name()
    category = ask_for_choice("Category:", CATEGORY_CHOICES)
    primary_purpose = ask_for_choice("Main purpose:", PURPOSE_CHOICES)
    warmth = ask_for_choice("Warmth level:", ATTRIBUTE_LEVELS)
    rain_protection = ask_for_choice("Rain protection level:", ATTRIBUTE_LEVELS)
    wind_protection = ask_for_choice("Wind protection level:", ATTRIBUTE_LEVELS)
    breathability = ask_for_choice("Breathability level:", ATTRIBUTE_LEVELS)

    return {
        "id": uuid4().hex,
        "name": name,
        "category": category,
        "primary_purpose": primary_purpose,
        "warmth": warmth,
        "rain_protection": rain_protection,
        "wind_protection": wind_protection,
        "breathability": breathability,
    }


def load_wardrobe(path=WARDROBE_PATH):
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as wardrobe_file:
        wardrobe = json.load(wardrobe_file)

    if not isinstance(wardrobe, list):
        raise ValueError("The wardrobe file must contain a list of clothing items.")

    return wardrobe


def save_wardrobe(items, path=WARDROBE_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as wardrobe_file:
        json.dump(items, wardrobe_file, indent=2)


def remove_clothing_item(items):
    if not items:
        print("\nYour wardrobe is empty, so there is nothing to remove.")
        return None

    print("\nChoose an item to remove:")

    for number, item in enumerate(items, start=1):
        category = item["category"].title()
        print(f'{number}. {item["name"]} — {category}')

    cancel_number = len(items) + 1
    print(f"{cancel_number}. Cancel")

    while True:
        answer = input("Choose a number: ").strip()

        if answer.isdigit():
            selected_number = int(answer)

            if selected_number == cancel_number:
                return None

            if 1 <= selected_number <= len(items):
                selected_item_id = items[selected_number - 1]["id"]

                for item_index, item in enumerate(items):
                    if item["id"] == selected_item_id:
                        return items.pop(item_index)

        print("Please choose one of the listed numbers.")


def manage_wardrobe(items, path=WARDROBE_PATH):
    while True:
        action = ask_for_choice("Wardrobe options:", WARDROBE_ACTIONS)

        if action == "continue":
            return items

        if action == "add":
            item = create_clothing_item()
            items.append(item)
            save_wardrobe(items, path)
            print(f'Added "{item["name"]}" to your wardrobe.')
            continue

        if action == "remove":
            removed_item = remove_clothing_item(items)

            if removed_item is not None:
                save_wardrobe(items, path)
                print(f'Removed "{removed_item["name"]}" from your wardrobe.')
