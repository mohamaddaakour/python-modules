class Plant:
    # constructor
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    # method
    def printing(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


# creating instances
rose = Plant("Rose", 25, 30)
violet = Plant("Sunflower", 80, 45)
tulip = Plant("Cactus", 15, 120)


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    rose.printing()
    violet.printing()
    tulip.printing()


if __name__ == "__main__":
    ft_garden_data()
