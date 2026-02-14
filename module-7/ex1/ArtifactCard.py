from ex0.Card import Card

class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self._durability = durability
        self._effect = effect

        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("Durability must be a positive integer")
        
    
    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self._name,
            'mana_used': self._cost,
            'effect': f'Permanent: {self._effect}'
        }
    
    def activate_ability(self) -> dict:
        return {
            'artifact': self._name,
            'ability': self._effect,
            'durability_remaining': self._durability,
            'activated': True
        }
    
    def get_card_info(self) -> dict:
        info = super().get_card_info()
        
        info['type'] = 'Artifact'
        info['durability'] = self._durability
        info['effect'] = self._effect
        
        return info