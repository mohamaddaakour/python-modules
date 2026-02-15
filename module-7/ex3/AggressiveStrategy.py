from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def __init__(self):
        self._total_damage = 0

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        targets_attacked = []
        damage_dealt = 0
        
        # Assume we have 10 mana available per turn
        available_mana = 10
        
        # Sort hand by cost (aggressive plays cheap cards fast)
        sorted_hand = sorted(hand, key=lambda card: card._cost)
        
        # Play as many cards as possible (low cost first)
        for card in sorted_hand:
            if card._cost <= available_mana:
                cards_played.append(card._name)
                mana_used += card._cost
                available_mana -= card._cost
                
                # If it's a creature, add its attack to damage
                if hasattr(card, '_attack_power'):
                    damage_dealt += getattr(card, '_attack_power', 3)
                # If it's a spell, add its power to damage
                elif hasattr(card, '_power'):
                    damage_dealt += getattr(card, '_power', 3)
        
        # Attack with creatures already on battlefield
        for card in battlefield:
            if hasattr(card, '_attack_power'):
                damage_dealt += getattr(card, '_attack_power', 3)
        
        # Prioritize attacking the enemy player
        if damage_dealt > 0:
            targets_attacked.append("Enemy Player")
        
        self._total_damage += damage_dealt
        
        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if not available_targets:
            return []
        
        prioritized = []
        
        # First priority: Enemy player
        players = [t for t in available_targets if 'Player' in str(t)]
        prioritized.extend(players)
        
        # Second priority: Weak creatures (easy to kill)
        creatures = [t for t in available_targets if 'Player' not in str(t)]
        
        # Sort by presumed strength (name length as proxy)
        creatures_sorted = sorted(creatures, key=lambda x: len(str(x)))
        prioritized.extend(creatures_sorted)
        
        return prioritized

    def get_total_damage(self) -> int:
        return self._total_damage