"""
TournamentCard - Card with tournament capabilities
Combines Card, Combatable, and Rankable using multiple inheritance
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from ex0.Card import Card
except ModuleNotFoundError:
    from Card import Card

try:
    from ex2.Combatable import Combatable
except ModuleNotFoundError:
    from Combatable import Combatable

try:
    from ex4.Rankable import Rankable
except ModuleNotFoundError:
    from Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    TournamentCard combines multiple interfaces for tournament play.
    
    Inherits from:
    - Card: Basic card functionality
    - Combatable: Combat abilities
    - Rankable: Tournament ranking
    
    This demonstrates advanced multiple inheritance for creating
    feature-rich game entities.
    """

    def __init__(self, name: str, cost: int, attack_power: int = 5, 
                 defense_rating: int = 3, starting_rating: int = 1200):
        """
        Initialize a tournament card.
        
        Args:
            name: Card name
            cost: Mana cost
            attack_power: Attack strength
            defense_rating: Defense strength
            starting_rating: Initial tournament rating (default 1200)
        """
        # Initialize Card parent
        super().__init__(name, cost)
        
        # Combat attributes (Combatable interface)
        self._attack_power = attack_power
        self._defense_rating = defense_rating
        self._health = 10
        self._max_health = 10
        
        # Ranking attributes (Rankable interface)
        self._rating = starting_rating
        self._wins = 0
        self._losses = 0
        self._matches_played = 0

    # Card interface implementation
    def play(self, game_state: dict) -> dict:
        """
        Play the card in a tournament context.
        
        Args:
            game_state: Current game state
        
        Returns:
            dict: Result of playing the card
        """
        return {
            'card_played': self._name,
            'cost': self._cost,
            'type': 'tournament',
            'rating': self._rating,
            'combat_ready': True,
            'tournament_stats': f'{self._wins}-{self._losses}'
        }

    # Combatable interface implementation
    def attack(self, target) -> dict:
        """
        Attack a target in combat.
        
        Args:
            target: The target to attack
        
        Returns:
            dict: Attack result
        """
        return {
            'attacker': self._name,
            'target': str(target),
            'damage': self._attack_power,
            'combat_type': 'tournament_match'
        }

    def defend(self, incoming_damage: int) -> dict:
        """
        Defend against incoming damage.
        
        Args:
            incoming_damage: Amount of damage to defend against
        
        Returns:
            dict: Defense result
        """
        damage_blocked = min(self._defense_rating, incoming_damage)
        damage_taken = incoming_damage - damage_blocked
        self._health = max(0, self._health - damage_taken)
        
        return {
            'defender': self._name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': self._health > 0
        }

    def get_combat_stats(self) -> dict:
        """
        Get combat statistics.
        
        Returns:
            dict: Combat stats
        """
        return {
            'name': self._name,
            'attack_power': self._attack_power,
            'defense_rating': self._defense_rating,
            'health': self._health,
            'max_health': self._max_health
        }

    # Rankable interface implementation
    def calculate_rating(self) -> int:
        """
        Calculate current rating.
        
        Rating calculation:
        - Base rating adjusted by win/loss ratio
        - Each win adds value, each loss subtracts value
        
        Returns:
            int: Current rating
        """
        return self._rating

    def update_wins(self, wins: int) -> None:
        """
        Update win count and adjust rating.
        
        Args:
            wins: Number of wins to add
        """
        self._wins += wins
        self._matches_played += wins
        # Increase rating based on wins (ELO-style: +16 per win)
        self._rating += wins * 16

    def update_losses(self, losses: int) -> None:
        """
        Update loss count and adjust rating.
        
        Args:
            losses: Number of losses to add
        """
        self._losses += losses
        self._matches_played += losses
        # Decrease rating based on losses (ELO-style: -16 per loss)
        self._rating -= losses * 16

    def get_rank_info(self) -> dict:
        """
        Get ranking information.
        
        Returns:
            dict: Ranking info
        """
        return {
            'name': self._name,
            'rating': self._rating,
            'wins': self._wins,
            'losses': self._losses,
            'matches_played': self._matches_played,
            'win_rate': self._wins / self._matches_played if self._matches_played > 0 else 0.0
        }

    # Additional tournament-specific methods
    def get_tournament_stats(self) -> dict:
        """
        Get comprehensive tournament statistics.
        
        Returns:
            dict: Combined stats from all interfaces
        """
        return {
            'card_info': self.get_card_info(),
            'combat_stats': self.get_combat_stats(),
            'rank_info': self.get_rank_info()
        }

    def reset_health(self) -> None:
        """Reset health for a new match."""
        self._health = self._max_health