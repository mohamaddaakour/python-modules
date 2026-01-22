def main():
    print("=== Achievement Tracker System ===")

    alice = set(["first_kill", "level_10", "treasure_hunter", "speed_demon", "first_kill"])
    bob = set(["first_kill", "level_10", "boss_slayer", "collector", "collector"])
    charlie = set([
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    ])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("=== Achievement Analytics ===")

    all_achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_all}")

    rare_achievements = all_achievements.difference(
        alice.intersection(bob)
        .union(alice.intersection(charlie))
        .union(bob.intersection(charlie))
    )
    print(f"Rare achievements (1 player): {rare_achievements}")

    alice_bob_common = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_unique = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")

if __name__ == "__main__":
    main()
