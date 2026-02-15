"""
SpellCard - A spell card implementation
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from ex0.Card import Card
except ModuleNotFoundError:
    from Card import Card


class SpellCard(Card):
    """
    Spell card that can be cast to produce magical effects.
    """

    def __init__(self, name: str, cost: int, effect: str = "damage"):
        """
        Initialize a spell card.
        
        Args:
            name: Spell name
            cost: Mana cost to cast
            effect: Effect type (damage, heal, buff, etc.)
        """
        super().__init__(name, cost)
        self._effect = effect
        self._power = cost  # Spell power equals cost

    def play(self, game_state: dict) -> dict:
        """
        Cast the spell.
        
        Args:
            game_state: Current game state
        
        Returns:
            dict: Result of casting the spell
        """
        return {
            'card_played': self._name,
            'cost': self._cost,
            'type': 'spell',
            'effect': self._effect,
            'power': self._power
        }