"""
DataDeck ex3 - Game Engine Demonstration
Shows Abstract Factory + Strategy Pattern combination
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from ex3.FantasyCardFactory import FantasyCardFactory
    from ex3.AggressiveStrategy import AggressiveStrategy
    from ex3.GameEngine import GameEngine
except ModuleNotFoundError:
    from FantasyCardFactory import FantasyCardFactory
    from AggressiveStrategy import AggressiveStrategy
    from GameEngine import GameEngine


def main():
    """Demonstrate the game engine with factory and strategy patterns."""
    
    print("=== DataDeck Game Engine ===\n")
    
    # Create factory and strategy
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    
    # Show supported types
    supported = factory.get_supported_types()
    print(f"Available types: {supported}\n")
    
    # Create and configure game engine
    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    
    # Show initial hand
    print("Simulating aggressive turn...")
    hand = engine.get_hand()
    hand_display = [f"{card._name} ({card._cost})" for card in hand]
    print(f"Hand: {hand_display}")
    
    # Simulate turn
    print("Turn execution:")
    turn_result = engine.simulate_turn()
    print(f"Strategy: {turn_result['strategy']}")
    print(f"Actions: {turn_result['actions']}\n")
    
    # Show game report
    print("Game Report:")
    status = engine.get_engine_status()
    print(f"{status}\n")
    
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!\n")
    print("How do Abstract Factory and Strategy patterns work together?")
    print("What makes this combination powerful for game engine systems?")


if __name__ == "__main__":
    main()