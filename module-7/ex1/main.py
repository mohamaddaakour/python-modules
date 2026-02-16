from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    # create a deck instance
    deck = Deck()

    # we create different types of cards
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

    # add the cards to deck
    deck.add_card(fire_dragon)
    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)

    # print the deck statistics
    print("Deck stats:", deck.get_deck_stats())

    print("")

    # shuffle the deck
    deck.shuffle()

    print("Drawing and playing cards:\n")

    while len(deck) > 0:
        card = deck.draw_card()

        if card:
            info = card.get_card_info()
            print(f"Drew: {info['name']} ({info['type']})")

            game_state = {}
            play_result = card.play(game_state)
            print(f"Play result: {play_result}")
            print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
