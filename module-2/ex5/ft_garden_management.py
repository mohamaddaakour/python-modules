class GardenError(Exception):
    """Base class for garden-related errors"""
    pass

class PlantError(GardenError):
    """Errors related to plants"""
    pass

class WaterError(GardenError):
    """Errors related to watering"""
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}

    def add_plant(self, name, water_level, sunlight_hours):
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")
            self.plants[name] = {'water': water_level, 'sun': sunlight_hours}
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant_name in self.plants:
                if plant_name == "failing_plant":
                    raise WaterError("Not enough water in tank")
                print(f"Watering {plant_name} - success")
        except WaterError as e:
            print(f"Caught GardenError: {e}")
            print("System recovered and continuing...")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self):
        print("Checking plant health...")
        for name, info in self.plants.items():
            try:
                water = info['water']
                sun = info['sun']
                if water < 1:
                    raise PlantError(f"Water level {water} is too low (min 1)")
                if water > 10:
                    raise PlantError(f"Water level {water} is too high (max 10)")
                if sun < 2:
                    raise PlantError(f"Sunlight hours {sun} is too low (min 2)")
                if sun > 12:
                    raise PlantError(f"Sunlight hours {sun} is too high (max 12)")
                print(f"{name}: healthy (water: {water}, sun: {sun})")
            except PlantError as e:
                print(f"Error checking {name}: {e}")


def test_garden_manager():
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("tomato", 5, 8)
    manager.add_plant("lettuce", 15, 6)
    manager.add_plant("", 5, 8)

    print("Watering plants...")
    manager.water_plants()

    manager.check_health()

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")

# if __name__ == "__main__":
#     test_garden_manager()
