class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self._height = 0
        self._age = 0

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days [OK]")

    def get_height(self) -> str:
        return self._height

    def get_age(self) -> int:
        return self._age


rose = SecurePlant("Rose")


def ft_garden_security():
    print("=== Garden Security System ===")
    print(f"Plant created: {rose.name}")

    rose.set_height(25)
    rose.set_age(30)

    print("")

    rose.set_height(-5)

    print("")

    print(f"Current plant: {rose.name} ({rose._height}cm, {rose._age} days)")


if __name__ == "__main__":
    ft_garden_security()
