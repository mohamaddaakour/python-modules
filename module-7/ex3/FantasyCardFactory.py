import sys
import os
import random

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from ex0.Card import Card
except ModuleNotFoundError:
    from Card import Card

try:
    from ex1.SpellCard import SpellCard
except ModuleNotFoundError:
    from SpellCard import SpellCard

try:
    from ex3.CardFactory import CardFactory
except ModuleNotFoundError:
    from CardFactory import CardFactory


class CreatureCard(Card):
    
    def __init__(self, name: str, cost: int, attack_power: int = 3):
        super().__init__(name, cost)
        self._attack_power = attack_power
    
    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self._name,
            'cost': self._cost,
            'type': 'creature',
            'attack_power': self._attack_power
        }


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, ability: str = "mana"):
        super().__init__(name, cost)
        self._ability = ability
    
    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self._name,
            'cost': self._cost,
            'type': 'artifact',
            'ability': self._ability
        }


class FantasyCardFactory(CardFactory):

    def __init__(self):
        """Initialize the fantasy card factory with card templates."""
        self._creature_templates = {
            'dragon': {'cost': 5, 'attack': 3, 'names': ['Fire Dragon', 'Ice Dragon', 'Shadow Dragon']},
            'goblin': {'cost': 2, 'attack': 2, 'names': ['Goblin Warrior', 'Goblin Scout', 'Goblin Shaman']}
        }
        
        self._spell_templates = {
            'fireball': {'cost': 3, 'effect': 'damage', 'names': ['Fireball', 'Greater Fireball']},
        }
        
        self._artifact_templates = {
            'mana_ring': {'cost': 2, 'ability': 'mana', 'names': ['Mana Ring', 'Ring of Power']},
            'staff': {'cost': 4, 'ability': 'spell_power', 'names': ['Magic Staff', 'Staff of Wisdom']},
            'crystal': {'cost': 3, 'ability': 'card_draw', 'names': ['Crystal Orb', 'Scrying Crystal']}
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            template_key = name_or_power.lower()
            if template_key in self._creature_templates:
                template = self._creature_templates[template_key]
                name = random.choice(template['names'])
                return CreatureCard(name, template['cost'], template['attack'])
        
        # Default: random creature
        creature_type = random.choice(list(self._creature_templates.keys()))
        template = self._creature_templates[creature_type]
        name = random.choice(template['names'])
        return CreatureCard(name, template['cost'], template['attack'])

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            template_key = name_or_power.lower()
            if template_key in self._spell_templates:
                template = self._spell_templates[template_key]
                name = random.choice(template['names'])
                return SpellCard(name, template['cost'], template['effect'])
        
        # Default: random spell
        spell_type = random.choice(list(self._spell_templates.keys()))
        template = self._spell_templates[spell_type]
        name = random.choice(template['names'])
        return SpellCard(name, template['cost'], template['effect'])

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            template_key = name_or_power.lower()
            if template_key in self._artifact_templates:
                template = self._artifact_templates[template_key]
                name = random.choice(template['names'])
                return ArtifactCard(name, template['cost'], template['ability'])
        
        # Default: random artifact
        artifact_type = random.choice(list(self._artifact_templates.keys()))
        template = self._artifact_templates[artifact_type]
        name = random.choice(template['names'])
        return ArtifactCard(name, template['cost'], template['ability'])

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        composition = {'creatures': 0, 'spells': 0, 'artifacts': 0}
        
        # Typical distribution: 50% creatures, 30% spells, 20% artifacts
        for i in range(size):
            roll = random.random()
            if roll < 0.5:
                deck.append(self.create_creature())
                composition['creatures'] += 1
            elif roll < 0.8:
                deck.append(self.create_spell())
                composition['spells'] += 1
            else:
                deck.append(self.create_artifact())
                composition['artifacts'] += 1
        
        return {
            'deck': deck,
            'size': size,
            'composition': composition,
            'theme': 'fantasy'
        }

    def get_supported_types(self) -> dict:
        return {
            'creatures': list(self._creature_templates.keys()),
            'spells': list(self._spell_templates.keys()),
            'artifacts': list(self._artifact_templates.keys())
        }