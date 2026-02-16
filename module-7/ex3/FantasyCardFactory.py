import random
from ex3.CardFactory import CardFactory


class Card:
    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost

    def __repr__(self):
        return f"{self.name} ({self.cost})"


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self._creature_types = {
            'dragon': {'names': ['Fire Dragon', 'Ice Dragon'], 'base_cost': 5},
            'goblin': {'names': ['Goblin Warrior', 'Goblin Shaman'],
                       'base_cost': 2}
        }
        self._spell_types = {
            'fireball': {'names': ['Fireball', 'Inferno'], 'base_cost': 3}
        }
        self._artifact_types = {
            'mana_ring': {'names': ['Mana Ring', 'Power Ring'], 'base_cost': 2}
        }

    def create_creature(self, name_or_power: str | int | None = None):
        creature_type = random.choice(list(self._creature_types.keys()))
        data = self._creature_types[creature_type]
        name = random.choice(data['names'])
        cost = data['base_cost']
        return Card(name, cost)

    def create_spell(self, name_or_power: str | int | None = None):
        spell_type = random.choice(list(self._spell_types.keys()))
        data = self._spell_types[spell_type]
        name = random.choice(data['names'])
        cost = data['base_cost']
        return Card(name, cost)

    def create_artifact(self, name_or_power: str | int | None = None):
        artifact_type = random.choice(list(self._artifact_types.keys()))
        data = self._artifact_types[artifact_type]
        name = random.choice(data['names'])
        cost = data['base_cost']
        return Card(name, cost)

    def create_themed_deck(self, size: int) -> dict:
        cards = []
        for _ in range(size):
            card_type = random.choice(['creature', 'spell', 'artifact'])
            if card_type == 'creature':
                cards.append(self.create_creature())
            elif card_type == 'spell':
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())
        return {'cards': cards, 'theme': 'Fantasy', 'size': len(cards)}

    def get_supported_types(self) -> dict:
        return {
            'creatures': list(self._creature_types.keys()),
            'spells': list(self._spell_types.keys()),
            'artifacts': list(self._artifact_types.keys())
        }
