"""
DataDeck ex4 - Tournament Platform Demonstration
Shows comprehensive tournament system with multiple inheritance
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from ex4.TournamentCard import TournamentCard
    from ex4.TournamentPlatform import TournamentPlatform
    from ex0.Card import Card
    from ex2.Combatable import Combatable
    from ex4.Rankable import Rankable
except ModuleNotFoundError:
    from TournamentCard import TournamentCard
    from TournamentPlatform import TournamentPlatform
    # Try to import for isinstance checks
    try:
        from Card import Card
        from Combatable import Combatable
        from Rankable import Rankable
    except:
        pass


def main():
    """Demonstrate the tournament platform."""
    
    print("=== DataDeck Tournament Platform ===\n")
    
    # Create tournament platform
    platform = TournamentPlatform()
    
    # Create tournament cards
    print("Registering Tournament Cards...")
    
    # Card 1: Fire Dragon
    dragon = TournamentCard("Fire Dragon", cost=5, attack_power=6, 
                           defense_rating=4, starting_rating=1200)
    dragon_id = platform.register_card(dragon)
    
    # Card 2: Ice Wizard
    wizard = TournamentCard("Ice Wizard", cost=4, attack_power=5, 
                           defense_rating=5, starting_rating=1150)
    wizard_id = platform.register_card(wizard)
    
    # Show card information
    print(f"{dragon._name} (ID: {dragon_id}):")
    print(f"- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.calculate_rating()}")
    print(f"- Record: {dragon._wins}-{dragon._losses}")
    print()
    
    print(f"{wizard._name} (ID: {wizard_id}):")
    print(f"- Interfaces: [Card, Combatable, Rankable]")
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
        print(f"{i}. {entry['name']} - Rating: {entry['rating']} ({entry['record']})")
    print()
    
    # Generate platform report
    print("Platform Report:")
    report = platform.generate_tournament_report()
    print(f"{report}")
    print()
    
    print("=== Tournament Platform Successfully Deployed! ===")
    print()
    print("All abstract patterns working together harmoniously!")
    print()
    print("How does multiple inheritance allow a class to implement several interfaces?")
    print("What are the benefits of combining ranking capabilities with card game mechanics?")


if __name__ == "__main__":
    main()