from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost:
                 int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self._attack = attack
        self._health = health

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self._name,
            "mana_used": self._cost,
            "effect": "Creature summoned to battlefield"
        }

    # the target here will be an instance
    def attack_target(self, target) -> dict:
        # check if the target object has an attribute called _name
        target_name = target._name if hasattr(target, "_name") else str(target)

        return {
            'attacker': self._name,
            'target': target_name,
            'damage_dealt': self._attack,
            'combat_resolved': True
        }

    def get_card_info(self) -> dict:
        # get card info from the parent class
        info = super().get_card_info()

        info['type'] = 'Creature'
        info['attack'] = self._attack
        info['health'] = self._health

        return info
