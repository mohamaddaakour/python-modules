from ex0.Card import Card
from typing import Optional
import random

class Deck:
    def __init__(self) -> None:
        self._cards: list[Card] = []
    
    def add_card(self, card: Card) -> None:
        self._cards.append(card)
    
    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self._cards):
            if card.get_card_info()['name'] == card_name:
                self._cards.pop(i)
                return True
        return False
    
    def shuffle(self) -> None:
        random.shuffle(self._cards)
    
    def draw_card(self) -> Optional[Card]:
        if self._cards:
            return self._cards.pop(0)
        return None
    
    def get_deck_stats(self) -> dict:
        if not self._cards:
            return {
                'total_cards': 0,
                'creatures': 0,
                'spells': 0,
                'artifacts': 0,
                'avg_cost': 0.0
            }
        
        creature_count = 0
        spell_count = 0
        artifact_count = 0
        total_cost = 0
        
        for card in self._cards:
            info = card.get_card_info()
            card_type = info.get('type', 'Unknown')
            
            if card_type == 'Creature':
                creature_count += 1
            elif card_type == 'Spell':
                spell_count += 1
            elif card_type == 'Artifact':
                artifact_count += 1
            
            total_cost += info['cost']
        
        avg_cost = total_cost / len(self._cards) if self._cards else 0.0
        
        return {
            'total_cards': len(self._cards),
            'creatures': creature_count,
            'spells': spell_count,
            'artifacts': artifact_count,
            'avg_cost': round(avg_cost, 1)
        }
    
    def __len__(self) -> int:
        return len(self._cards)
    
    def __repr__(self) -> str:
        stats = self.get_deck_stats()
        return f"Deck({stats['total_cards']} cards)"