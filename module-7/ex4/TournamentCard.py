from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity, attack_power: int = 5,
                 defense_rating: int = 3, starting_rating: int = 1200):
        # Initialize Card parent
        super().__init__(name, cost, rarity)

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
        return {
            'attacker': self._name,
            'target': str(target),
            'damage': self._attack_power,
            'combat_type': 'tournament_match'
        }

    def defend(self, incoming_damage: int) -> dict:
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
        return {
            'name': self._name,
            'attack_power': self._attack_power,
            'defense_rating': self._defense_rating,
            'health': self._health,
            'max_health': self._max_health
        }

    # Rankable interface implementation
    def calculate_rating(self) -> int:
        return self._rating

    def update_wins(self, wins: int) -> None:
        self._wins += wins
        self._matches_played += wins
        # Increase rating based on wins (ELO-style: +16 per win)
        self._rating += wins * 16

    def update_losses(self, losses: int) -> None:
        self._losses += losses
        self._matches_played += losses
        # Decrease rating based on losses (ELO-style: -16 per loss)
        self._rating -= losses * 16

    def get_rank_info(self) -> dict:
        return {
            'name': self._name,
            'rating': self._rating,
            'wins': self._wins,
            'losses': self._losses,
            'matches_played': self._matches_played,
            'win_rate':
            self._wins / self._matches_played
            if self._matches_played > 0 else 0.0
        }

    # Additional tournament-specific methods
    def get_tournament_stats(self) -> dict:
        return {
            'card_info': self.get_card_info(),
            'combat_stats': self.get_combat_stats(),
            'rank_info': self.get_rank_info()
        }

    def reset_health(self) -> None:
        self._health = self._max_health
