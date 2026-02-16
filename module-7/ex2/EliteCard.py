from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity, attack_power: int = 5, defense_rating: int = 5, mana_pool: int = 10):
        super().__init__(name, cost, rarity)
        self._attack_power = attack_power
        self._defense_rating = defense_rating
        self._health = 10
        self._max_health = 10
        self._mana_pool = mana_pool
        self._max_mana = mana_pool
        self._available_spells = ['Fireball', 'Lightning Bolt', 'Shield', 'Heal']
        self._rarity = rarity

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self._name,
            'cost': self._cost,
            'type': 'elite',
            'effects': 'Combat and Magic abilities activated',
            'combat_ready': True,
            'magic_ready': True
        }

    def attack(self, target) -> dict:
        return {
            'attacker': self._name,
            'target': str(target),
            'damage': self._attack_power,
            'combat_type': 'melee'
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

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost_map = {
            'Fireball': 4,
            'Lightning Bolt': 3,
            'Shield': 2,
            'Heal': 3
        }

        mana_cost = mana_cost_map.get(spell_name, 5)

        if spell_name not in self._available_spells:
            return {
                'caster': self._name,
                'spell': spell_name,
                'success': False,
                'reason': 'Spell not available'
            }

        if self._mana_pool < mana_cost:
            return {
                'caster': self._name,
                'spell': spell_name,
                'success': False,
                'reason': 'Insufficient mana'
            }

        self._mana_pool -= mana_cost

        return {
            'caster': self._name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': mana_cost
        }

    def channel_mana(self, amount: int) -> dict:
        actual_channeled = min(amount, self._max_mana - self._mana_pool)
        self._mana_pool += actual_channeled

        return {
            'channeled': actual_channeled,
            'total_mana': self._mana_pool
        }

    def get_magic_stats(self) -> dict:
        return {
            'name': self._name,
            'mana_pool': self._mana_pool,
            'max_mana': self._max_mana,
            'available_spells': self._available_spells.copy(),
            'spell_count': len(self._available_spells)
        }
