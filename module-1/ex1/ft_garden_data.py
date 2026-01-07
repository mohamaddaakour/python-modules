class Plant:
    # constructor
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    # method
    def printing(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

# creating instances
rose = Plant("Rose", 25, 35)
violet = Plant("Violet", 30, 75)
tulip = Plant("Tulip", 45, 85)

def ft_garden_data():
    print("=== Garden Plant Registry ===")
    rose.printing()
    violet.printing()
    tulip.printing()

# ft_garden_data()
