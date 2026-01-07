class Plant:
    # attribute
    plants = []

    # constructor
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.plant_age = age

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.plant_age} days)")

# factory function
def  ft_plant_factory():
    plants = []

    print("=== Plant Factory Output ===")

    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    for name, height, age in plant_data:
        plants.append(Plant(name, height, age))

    for i in plants:
        i.get_info()

    print(f"Total plants created: {len(plants)}")

ft_plant_factory()
