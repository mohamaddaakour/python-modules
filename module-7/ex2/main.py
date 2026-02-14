from EliteCard import EliteCard


def main():
    
    print("=== DataDeck Ability System ===\n")
    
    # elite card instance
    elite = EliteCard("Arcane Warrior", cost=5, attack_power=5, defense_rating=3, mana_pool=10)
    
    print("EliteCard capabilities:")
    
    card_methods = ['play', 'get_card_info', 'is_playable']
    print(f"- Card: {card_methods}")
    
    combat_methods = ['attack', 'defend', 'get_combat_stats']
    print(f"- Combatable: {combat_methods}")
    
    magic_methods = ['cast_spell', 'channel_mana', 'get_magic_stats']
    print(f"- Magical: {magic_methods}")
    
    print()
    
    print(f"Playing {elite._name} (Elite Card):")
    print()
    
    print("Combat phase:")
    attack_result = elite.attack("Enemy")
    print(f"Attack result: {attack_result}")
    
    defend_result = elite.defend(5)
    print(f"Defense result: {defend_result}")
    print()
    
    print("Magic phase:")
    spell_result = elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_result}")
    
    mana_result = elite.channel_mana(3)
    print(f"Mana channel: {mana_result}")
    print()
    
    print("Multiple interface implementation successful!")
    print()
    print("How do multiple interfaces enable flexible card design?")
    print("What are the advantages of separating combat and magic concerns?")


if __name__ == "__main__":
    main()