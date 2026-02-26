# we sort the list in descending order for the power values in each dictionary
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda artifact: artifact["power"], reverse=True)


# we filter the list with the dictionary having
# power greater or equal the min_power
def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


# each element in the list we will apply on it this operation
def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    avg_power = round(
        sum(map(lambda mage: mage["power"], mages)) / len(mages), 2
    )

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":

    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "Mystic"},
        {"name": "Fire Staff", "power": 92, "type": "Elemental"},
        {"name": "Shadow Dagger", "power": 78, "type": "Dark"}
    ]

    map_list = spell_transformer(["hello", "world"])
    print(map_list)

    mages = [
        {"name": "Aelar", "power": 90, "element": "Fire"},
        {"name": "Lyra", "power": 75, "element": "Water"},
        {"name": "Thorne", "power": 60, "element": "Earth"}
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']}"
          f"({sorted_artifacts[0]['power']} power) "
          f"comes before {sorted_artifacts[1]['name']}"
          f"({sorted_artifacts[1]['power']} power)")

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nTesting mage stats...")
    print(mage_stats(mages))
