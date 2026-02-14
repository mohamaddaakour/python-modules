"""
main.py - Demonstration of the DataDeck Deck Builder
Shows how polymorphism enables different card types to work together.
"""

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    """Demonstrate the deck builder system with polymorphism."""
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...\n")
    
    # Create a deck
    deck = Deck()
    
    # Create different card types - all inherit from Card
    fire_dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )
    
    lightning_bolt = SpellCard(
        name="Lightning Bolt",
        cost=3,
        rarity="Common",
        effect_type="damage"
    )
    
    mana_crystal = ArtifactCard(
        name="Mana Crystal",
        cost=2,
        rarity="Rare",
        durability=5,
        effect="+1 mana per turn"
    )
    
    # Add cards to deck - polymorphism in action!
    # The deck accepts any Card type through the common interface
    deck.add_card(fire_dragon)
    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)
    
    # Display deck statistics
    print("Deck stats:", deck.get_deck_stats())
    print()
    
    # Shuffle the deck
    deck.shuffle()
    
    # Draw and play cards
    print("Drawing and playing cards:\n")
    
    while len(deck) > 0:
        # Draw a card - could be any type!
        card = deck.draw_card()
        
        if card:
            # Get card info polymorphically
            info = card.get_card_info()
            print(f"Drew: {info['name']} ({info['type']})")
            
            # Play the card - each type implements play() differently!
            game_state = {}
            play_result = card.play(game_state)
            print(f"Play result: {play_result}")
            print()
    
    print("Polymorphism in action: Same interface, different card behaviors!")
    print()
    
    # Demonstrate polymorphism benefits
    print("=== Polymorphism Demonstration ===\n")
    
    # Create a new deck
    demo_deck = Deck()
    
    # Add various cards
    demo_deck.add_card(CreatureCard("Goblin", 2, "Common", 2, 2))
    demo_deck.add_card(SpellCard("Fireball", 4, "Uncommon", "damage"))
    demo_deck.add_card(ArtifactCard("Shield", 3, "Rare", 3, "+2 defense"))
    demo_deck.add_card(CreatureCard("Dragon", 6, "Legendary", 8, 6))
    demo_deck.add_card(SpellCard("Heal", 2, "Common", "heal"))
    
    print(f"Created deck with {len(demo_deck)} cards")
    print(f"Stats: {demo_deck.get_deck_stats()}")
    print()
    
    # Test remove functionality
    print("Removing 'Goblin' from deck...")
    removed = demo_deck.remove_card("Goblin")
    print(f"Removed: {removed}")
    print(f"New stats: {demo_deck.get_deck_stats()}")
    print()
    
    # Draw a few cards
    print("Drawing 3 cards:")
    for i in range(3):
        card = demo_deck.draw_card()
        if card:
            info = card.get_card_info()
            print(f"  {i+1}. {info['name']} ({info['type']}) - Cost: {info['cost']}")
    
    print()
    print(f"Remaining cards in deck: {len(demo_deck)}")


if __name__ == "__main__":
    main()