def spell_combiner(spell1: callable, spell2: callable) -> callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Both arguments must be callable")

    def combined(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))

    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    if not callable(base_spell):
        raise TypeError("base_spell must be callable")

    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier

    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    if not callable(condition) or not callable(spell):
        raise TypeError("Both condition and spell must be callable")

    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"

    return caster


def spell_sequence(spells: list[callable]) -> callable:
    for spell in spells:
        if not callable(spell):
            raise TypeError("All elements must be callable")

    def sequence(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results

    return sequence


if __name__ == "__main__":

    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    def damage_spell(amount):
        return amount

    def is_alive(target):
        return target != "Ghost"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result:", combined("Dragon"))

    print("\nTesting power amplifier...")
    amplified = power_amplifier(damage_spell, 3)
    print("Original:", damage_spell(10), "Amplified:", amplified(10))

    print("\nTesting conditional caster...")
    conditional_spell = conditional_caster(is_alive, fireball)
    print("Alive target:", conditional_spell("Knight"))
    print("Dead target:", conditional_spell("Ghost"))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print("Sequence result:", sequence("Dragon"))