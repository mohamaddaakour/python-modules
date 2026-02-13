def validate_ingredients(ingredients: str) -> str:
    valid_elements = ["fire", "earth", "water", "air"]

    for element in ingredients.split():
        if element not in valid_elements:
            return f"{ingredients} - INVALID"

    return f"{ingredients} - VALID"