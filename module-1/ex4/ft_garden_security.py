class SecurePlant:
    def __init__(self, name):
        self.name = name
        self.height = 0
        self.age = 0

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.height = height
        print(f"Height updated: {self.height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.age = age
        print(f"Age updated: {self.age} days [OK]")

    def get_height(self):
        return self.height

    def get_age(self):
        return self.age


rose = SecurePlant("Rose")

def ft_garden_security():
    print("=== Garden Security System ===")
    print(f"Plant created: {rose.name}")

    rose.set_height(25)
    rose.set_age(20)
    rose.set_height(-5)

    print(f"Current plant: {rose.name} ({rose.height}cm, {rose.age} days)")


if __name__ == "__main__":
    ft_garden_security()
