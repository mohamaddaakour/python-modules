from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")

    # we create an instance of creature card
    fire_dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )

    print(fire_dragon.get_card_info())

    print("")

    print("Playing Fire Dragon with 6 mana available:")
    available_mana = 6
    is_playable = fire_dragon.is_playable(available_mana)
    print(f"Playable: {is_playable}")

    if is_playable:
        game_state = {}
        play_result = fire_dragon.play(game_state)
        print(f"Play result: {play_result}")

    print("")

    print("Fire Dragon attacks Goblin Warrior:")

    # we create another instance of creature card to attack him
    goblin = CreatureCard(
        name="Goblin Warrior",
        cost=2,
        rarity="Common",
        attack=2,
        health=2
    )

    # the fire dragon attacked the goblin
    attack_result = fire_dragon.attack_target(goblin)

    print(f"Attack result: {attack_result}")

    print("")

    # if we don't have enough mana
    print("Testing insufficient mana (3 available):")
    insufficient_mana = 3
    is_playable = fire_dragon.is_playable(insufficient_mana)
    print(f"Playable: {is_playable}")

    print("")

    print("Abstract pattern successfully demonstrated!")


main()
