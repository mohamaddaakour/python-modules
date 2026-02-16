from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self):
        self._factory = None
        self._strategy = None
        self._turns_simulated = 0
        self._total_damage = 0
        self._cards_created = 0

    def configure_engine(self, factory:
                         CardFactory, strategy: GameStrategy) -> None:
        self._factory = factory
        self._strategy = strategy
        print("\nConfiguring Fantasy Card Game...")
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Available types: {factory.get_supported_types()}")

    def simulate_turn(self) -> dict:
        if not self._factory or not self._strategy:
            raise RuntimeError("Engine not configured")

        hand = [
            self._factory.create_creature(),
            self._factory.create_creature(),
            self._factory.create_spell()
        ]
        self._cards_created += len(hand)

        print("\nSimulating aggressive turn...")
        print(f"Hand: {hand}")

        turn_result = self._strategy.execute_turn(hand, [])
        self._turns_simulated += 1
        self._total_damage += turn_result.get('damage_dealt', 0)

        print("\nTurn execution:")
        print(f"Strategy: {self._strategy.get_strategy_name()}")
        print(f"Actions: {turn_result}")

        return turn_result

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self._turns_simulated,
            'strategy_used':
            self._strategy.get_strategy_name() if self._strategy else 'None',
            'total_damage': self._total_damage,
            'cards_created': self._cards_created
        }
