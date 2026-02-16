# import sys
# import os

# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print(f"Factory: FantasyCardFactory")
    print(f"Strategy: {strategy.get_strategy_name()}")

    supported = factory.get_supported_types()
    print(f"Available types: {supported}\n")

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Simulating aggressive turn...")
    hand = engine.get_hand()
    hand_display = [f"{card._name} ({card._cost})" for card in hand]
    print(f"Hand: {hand_display}")

    print("Turn execution:")
    turn_result = engine.simulate_turn()
    print(f"Strategy: {turn_result['strategy']}")
    print(f"Actions: {turn_result['actions']}\n")

    print("Game Report:")
    status = engine.get_engine_status()
    print(f"{status}\n")

if __name__ == "__main__":
    main()
