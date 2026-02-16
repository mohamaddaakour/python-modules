from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():

    print("=== DataDeck Tournament Platform ===\n")

    # Create tournament platform
    platform = TournamentPlatform()

    # Create tournament cards
    print("Registering Tournament Cards...")

    # Card : Fire Dragon
    dragon = TournamentCard("Fire Dragon", cost=5, attack_power=6,
                            defense_rating=4, starting_rating=1200, rarity=1)
    dragon_id = platform.register_card(dragon)

    # Card : Ice Wizard
    wizard = TournamentCard("Ice Wizard", rarity=1, cost=4, attack_power=5,
                            defense_rating=5, starting_rating=1150)
    wizard_id = platform.register_card(wizard)

    # Show card information
    print(f"{dragon._name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.calculate_rating()}")
    print(f"- Record: {dragon._wins}-{dragon._losses}")
    print()

    print(f"{wizard._name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.calculate_rating()}")
    print(f"- Record: {wizard._wins}-{wizard._losses}")
    print()

    # Create a match
    print("Creating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")
    print()

    # Show leaderboard
    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, entry in enumerate(leaderboard, 1):
        print(f"{i}. {entry['name']} - "
              f"Rating: {entry['rating']} ({entry['record']})")

    print("")

    # Generate platform report
    print("Platform Report:")
    report = platform.generate_tournament_report()
    print(f"{report}")

    print("")

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
