from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        targets_attacked = []
        damage_dealt = 0

        sorted_hand = sorted(hand, key=lambda card: card.cost)

        available_mana = 10
        for card in sorted_hand:
            if card.cost <= available_mana:
                cards_played.append(card.name)
                mana_used += card.cost
                available_mana -= card.cost
                damage_dealt += card.cost

        if cards_played:
            targets_attacked.append('Enemy Player')

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        prioritized = []
        for target in available_targets:
            if 'Player' in str(target):
                prioritized.insert(0, target)
            else:
                prioritized.append(target)
        return prioritized
