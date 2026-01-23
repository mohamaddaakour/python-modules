class Plant:
    # constructor
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    # methods
    def grow(self) -> None:
        self.height += 6

    def age(self) -> None:
        self.plant_age += 6

    def get_info(self) -> None:
        print("=== Day 1 ===")
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")

        self.grow()
        self.age()

        print("=== Day 7 ===")
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")
        print("Growth this week: +6cm")


rose = Plant("Rose", 25, 35)
violet = Plant("Violet", 30, 75)
tulip = Plant("Tulip", 45, 85)


def ft_plant_growth() -> None:
    rose.get_info()
    violet.get_info()
    tulip.get_info()


if __name__ == "__main__":
    ft_plant_growth()
