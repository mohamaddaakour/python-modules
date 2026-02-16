

# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy

# try:

# except ModuleNotFoundError:
#     from CardFactory import CardFactory
#     from GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        """Initialize the game engine."""
        self._factory = None
        self._strategy = None
        self._hand = []
        self._battlefield = []
        self._turns_simulated = 0
        self._total_damage = 0
        self._cards_created = 0

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        """
        Configure the game engine with a factory and strategy.

        Args:
            factory: CardFactory instance for creating cards
            strategy: GameStrategy instance for game decisions
        """
        self._factory = factory
        self._strategy = strategy

        # Initialize a starting hand with specific cards for demo
        # Create a Fire Dragon (5 cost)
        dragon = factory.create_creature('dragon')
        dragon._name = 'Fire Dragon'
        dragon._cost = 5

        # Create a Goblin Warrior (2 cost)
        goblin = factory.create_creature('goblin')
        goblin._name = 'Goblin Warrior'
        goblin._cost = 2

        # Create Lightning Bolt spell (3 cost)
        spell = factory.create_spell('fireball')
        spell._name = 'Lightning Bolt'
        spell._cost = 3

        self._hand = [dragon, goblin, spell]
        self._cards_created = len(self._hand)

    def simulate_turn(self) -> dict:
        """
        Simulate a single turn using the configured strategy.

        Returns:
            dict: Turn simulation results
        """
        if not self._factory or not self._strategy:
            return {'error': 'Engine not configured'}

        # Execute turn using strategy
        turn_result = self._strategy.execute_turn(self._hand, self._battlefield)

        # Update game state
        self._turns_simulated += 1
        self._total_damage += turn_result.get('damage_dealt', 0)

        # Move played cards to battlefield
        played_card_names = turn_result.get('cards_played', [])
        cards_to_move = []
        for card in self._hand[:]:
            if card._name in played_card_names:
                cards_to_move.append(card)
                self._hand.remove(card)

        self._battlefield.extend(cards_to_move)

        return {
            'turn_number': self._turns_simulated,
            'strategy': self._strategy.get_strategy_name(),
            'actions': turn_result,
            'hand_size': len(self._hand),
            'battlefield_size': len(self._battlefield)
        }

    def get_engine_status(self) -> dict:
        """
        Get current engine status.

        Returns:
            dict: Engine status information
        """
        return {
            'turns_simulated': self._turns_simulated,
            'strategy_used': self._strategy.get_strategy_name() if self._strategy else None,
            'total_damage': self._total_damage,
            'cards_created': self._cards_created,
            'hand_size': len(self._hand),
            'battlefield_size': len(self._battlefield)
        }

    def get_hand(self) -> list:
        """Get current hand."""
        return self._hand

    def get_battlefield(self) -> list:
        """Get current battlefield."""
        return self._battlefield
