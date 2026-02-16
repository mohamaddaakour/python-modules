"""
Fixed FantasyCardFactory implementation with create_themed_deck method
"""

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex3.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.creature_templates = {
            'dragon': {
                'attack': 7,
                'defense': 5,
                'cost': 6,
                'creature_type': 'flying'
            },
            'goblin': {
                'attack': 2,
                'defense': 1,
                'cost': 1,
                'creature_type': 'ground'
            }
        }

        # Spell templates - FIX: Added 'effect_type' field
        self.spell_templates = {
            'fireball': {
                'cost': 3,
                'effect': 'Deal 4 damage to target',
                'effect_type': 'damage'
            }
        }

        # Artifact templates
        self.artifact_templates = {
            'mana_ring': {
                'cost': 2,
                'effect': 'Gain 1 mana per turn',
                'durability': 5
            },
            'staff': {
                'cost': 3,
                'effect': 'Increase spell power by 2',
                'durability': 4
            },
            'crystal': {
                'cost': 1,
                'effect': 'Store 3 mana',
                'durability': 3
            }
        }

    def create_creature(self, creature_type: str) -> CreatureCard:
        """Create a creature card"""
        if creature_type not in self.creature_templates:
            raise ValueError(f"Unknown creature type: {creature_type}")

        template = self.creature_templates[creature_type]
        return CreatureCard(
            creature_type,
            template['cost'],
            template['attack'],
            template['defense'],
            template['creature_type']
        )

    def create_spell(self, spell_type: str) -> SpellCard:
        """Create a spell card - FIXED VERSION"""
        if spell_type not in self.spell_templates:
            raise ValueError(f"Unknown spell type: {spell_type}")

        template = self.spell_templates[spell_type]
        # FIX: Pass all 4 required arguments including effect_type
        return SpellCard(
            spell_type,
            template['cost'],
            template['effect'],
            template['effect_type']
        )

    def create_artifact(self, artifact_type: str) -> ArtifactCard:
        """Create an artifact card"""
        if artifact_type not in self.artifact_templates:
            raise ValueError(f"Unknown artifact type: {artifact_type}")

        template = self.artifact_templates[artifact_type]
        return ArtifactCard(
            artifact_type,
            template['cost'],
            template['effect'],
            template['durability']
        )

    def create_themed_deck(self, theme: str) -> list:
        """
        Create a themed deck of cards.

        Args:
            theme: The theme name (e.g., 'aggressive', 'defensive', 'balanced')

        Returns:
            List of Card objects forming a themed deck
        """
        deck = []

        if theme == 'aggressive':
            # Aggressive deck: more creatures and damage spells
            deck.append(self.create_creature('dragon'))
            deck.append(self.create_creature('goblin'))
            deck.append(self.create_creature('goblin'))
            deck.append(self.create_spell('fireball'))
            deck.append(self.create_spell('fireball'))
            deck.append(self.create_artifact('staff'))

        elif theme == 'defensive':
            # Defensive deck: more artifacts and fewer aggressive creatures
            deck.append(self.create_creature('dragon'))
            deck.append(self.create_artifact('mana_ring'))
            deck.append(self.create_artifact('crystal'))
            deck.append(self.create_artifact('staff'))
            deck.append(self.create_spell('fireball'))

        elif theme == 'balanced':
            # Balanced deck: mix of everything
            deck.append(self.create_creature('dragon'))
            deck.append(self.create_creature('goblin'))
            deck.append(self.create_spell('fireball'))
            deck.append(self.create_artifact('mana_ring'))
            deck.append(self.create_artifact('crystal'))

        else:
            # Default deck
            deck.append(self.create_creature('goblin'))
            deck.append(self.create_spell('fireball'))
            deck.append(self.create_artifact('crystal'))

        return deck

    def get_supported_types(self) -> dict:
        """Return all supported card types"""
        return {
            'creatures': list(self.creature_templates.keys()),
            'spells': list(self.spell_templates.keys()),
            'artifacts': list(self.artifact_templates.keys())
        }
