class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def describe(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: int) -> None:
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def describe(self) -> str:
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 prize_points: int) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def describe(self) -> str:
        return (
            f"{self.name}: {self.height}cm, {self.color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
        )


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.total_growth = 0

    def add_plant(self, plant: str) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def report(self, stats_helper: str) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.describe()}")

        stats = stats_helper.calculate(self.plants, self.total_growth)
        print(f"Plants added: {stats['count']}, "
              f"Total growth: {stats['growth']}cm")
        print(
            f"Plant types: {stats['regular']} regular, "
            f"{stats['flowering']} flowering, "
            f"{stats['prize']} prize flowers"
        )


class GardenManager:
    gardens = []

    class GardenStats:
        def calculate(self, plants: str, growth: int) -> dict:
            regular = 0
            flowering = 0
            prize = 0

            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1

            return {
                "count": len(plants),
                "growth": growth,
                "regular": regular,
                "flowering": flowering,
                "prize": prize,
            }

    def add_garden(self, garden: str) -> None:
        GardenManager.gardens.append(garden)

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    @classmethod
    def create_garden_network(cls) -> None:
        scores = {}
        for garden in cls.gardens:
            score = 0
            for plant in garden.plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points
            scores[garden.owner] = score

        score_output = ", ".join(
            [f"{owner}: {score}" for owner, score in scores.items()]
        )
        print(f"Garden scores - {score_output}")
        print(f"Total gardens managed: {len(cls.gardens)}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    manager = GardenManager()
    stats = GardenManager.GardenStats()

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.grow_all()
    alice_garden.report(stats)

    print(f"Height validation test: {GardenManager.validate_height(10)}")

    bob_garden.add_plant(Plant("Pine Tree", 80))
    bob_garden.grow_all()

    GardenManager.create_garden_network()
