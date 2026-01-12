class GardenError(Exception):
    """Base class for garden-related errors"""
    pass

class PlantError(GardenError):
    """Error related to plants"""
    pass

class WaterError(GardenError):
    """Error related to watering"""
    pass


def check_plant():
    raise PlantError("The tomato plant is wilting!")

def check_water():
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    for func in [check_plant, check_water]:
        try:
            func()
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("All custom error types work correctly!")

# if __name__ == "__main__":
#     test_custom_errors()
