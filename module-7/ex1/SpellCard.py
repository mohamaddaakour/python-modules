from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self._effect_type = effect_type

    def play(self, game_state: dict) -> dict:
    
        effect_descriptions = {
            'damage': f'Deal {self._cost} damage to target',
            'heal': f'Heal {self._cost} health to target',
            'buff': f'Grant +{self._cost}/+{self._cost} to target creature',
            'debuff': f'Reduce target by -{self._cost}/-{self._cost}'
        }

        effect_text = effect_descriptions.get(self._effect_type)

        effect_text += f'{self._effect_type.capitalize()} effect applied'

        return {
            'card_played': self._name,
            'mana_used': self._cost,
            'effect': effect_text
        }

    def resolve_effect(self, targets: list) -> dict:
        target_names = []
        for target in targets:
            if hasattr(target, '_name'):
                target_names.append(target._name)
            else:
                target_names.append(str(target))
        
        return {
            'spell': self._name,
            'effect_type': self._effect_type,
            'targets': target_names,
            'resolved': True,
            'consumed': True
        }
    
    def get_card_info(self) -> dict:
        info = super().get_card_info()
        
        info['type'] = 'Spell'
        info['effect_type'] = self._effect_type
        
        return info