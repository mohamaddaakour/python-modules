from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self._cards = {}
        self._matches_played = 0
        self._match_history = []
        self._id_counters = {}

    def register_card(self, card: TournamentCard) -> str:
        name_parts = card._name.lower().split()
        if len(name_parts) >= 2:
            base_id = name_parts[1]
        else:
            base_id = name_parts[0]

        # Increment counter for this type
        if base_id not in self._id_counters:
            self._id_counters[base_id] = 0
        self._id_counters[base_id] += 1

        card_id = f"{base_id}_{str(self._id_counters[base_id]).zfill(3)}"

        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self._cards or card2_id not in self._cards:
            return {'error': 'Invalid card ID(s)'}

        card1 = self._cards[card1_id]
        card2 = self._cards[card2_id]

        # Reset health for new match
        card1.reset_health()
        card2.reset_health()

        # Simulate match (simple combat simulation)
        winner_id, loser_id = self._simulate_combat(
            card1_id, card1, card2_id, card2
        )

        winner = self._cards[winner_id]
        loser = self._cards[loser_id]

        # Update wins and losses
        winner.update_wins(1)
        loser.update_losses(1)

        # Record match
        self._matches_played += 1
        match_result = {
            'match_number': self._matches_played,
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating':
            winner.calculate_rating(),
            'loser_rating': loser.calculate_rating()
        }

        self._match_history.append(match_result)

        return match_result

    def _simulate_combat(self, card1_id: str, card1: TournamentCard,
                         card2_id: str, card2: TournamentCard) -> tuple:
        # Combat based on attack power (higher attack wins)
        # In case of tie, first card wins
        if card1._attack_power >= card2._attack_power:
            return (card1_id, card2_id)
        else:
            return (card2_id, card1_id)

    def get_leaderboard(self) -> list:
        leaderboard = []

        for card_id, card in self._cards.items():
            rank_info = card.get_rank_info()
            leaderboard.append({
                'id': card_id,
                'name': card._name,
                'rating': rank_info['rating'],
                'wins': rank_info['wins'],
                'losses': rank_info['losses'],
                'record': f"{rank_info['wins']}-{rank_info['losses']}"
            })

        # Sort by rating (highest first)
        leaderboard.sort(key=lambda x: x['rating'], reverse=True)

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self._cards)

        if total_cards == 0:
            return {
                'total_cards': 0,
                'matches_played': 0,
                'avg_rating': 0,
                'platform_status': 'empty'
            }

        # Calculate average rating
        total_rating = sum(
            card.calculate_rating() for card in self._cards.values()
        )
        avg_rating = total_rating // total_cards

        return {
            'total_cards': total_cards,
            'matches_played': self._matches_played,
            'avg_rating': avg_rating,
            'platform_status': (
                'active' if self._matches_played > 0 else 'initialized'
            )
        }

    def get_card(self, card_id: str) -> TournamentCard:
        return self._cards.get(card_id)

    def get_all_cards(self) -> dict:
        return self._cards.copy()
