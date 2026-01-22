class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days"


# Flower subclass
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        return f"{self.name} (Flower): {self.height}cm"
        f", {self.age} days, {self.color} color"


# Tree subclass
class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = self.height * self.trunk_diameter / 10
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")

    def get_info(self):
        return f"{self.name} (Tree): {self.height}cm"
        f", {self.age} days, {self.trunk_diameter}cm diameter"


# Vegetable subclass
class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        return f"{self.name} (Vegetable): {self.height}cm"
        f", {self.age} days, {self.harvest_season} harvest"

    def nutrition_info(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


# Create plant instances
def ft_garden_plant_types():
    print("=== Garden Plant Types ===")

    print("")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 300, 1500, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 60, "fall", "vitamin A")

    for plant in [rose, tulip, oak, pine, tomato, carrot]:
        print(plant.get_info())
        if isinstance(plant, Flower):
            plant.bloom()
            print("")
        elif isinstance(plant, Tree):
            plant.produce_shade()
            print("")
        elif isinstance(plant, Vegetable):
            plant.nutrition_info()
            print("")


if __name__ == "__main__":
    ft_garden_plant_types()
