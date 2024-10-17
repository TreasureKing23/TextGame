class Spell:
    def __init__(self, name: str, spell_type: str, mana_cost: int) -> None:
        self.name = name
        self.type = spell_type
        self.mana_cost = mana_cost

    def cast(self, caster, target):
        raise NotImplementedError("Each spell needs a specific cast method")
    
class DamageSpell(Spell):
    def __init__(self, name: str, spell_type: str, mana_cost: int, damage: int) -> None:
        super().__init__(name, spell_type, mana_cost)
        self.damage = damage

    def cast(self, caster, target) -> None:
        if caster.mana >= self.mana_cost:
            caster.mana -= self.mana_cost
            target.health -= self.damage
            target.health = max(target.health, 0)
            print(f"{caster.name} casts {self.name} on {target.name}, dealing {self.damage} damage!")
            print(f"{target.name}'s health is now {target.health}")
            print(f"{caster.name}'s mana is now {caster.mana}")
        else:
            print(f"{caster.name} does not have enough mana to cast {self.name}.")


class HealingSpell(Spell):
    def __init__(self, name: str, spell_type: str, mana_cost: int, heal_amount: int) -> None:
        super().__init__(name, spell_type, mana_cost)
        self.heal_amount = heal_amount

    def cast(self, caster, target) -> None:
        if caster.mana >= self.mana_cost:
            caster.mana -= self.mana_cost
            target.health += self.heal_amount
            print(f"{caster.name} casts {self.name} on {target.name}, restoring {self.heal_amount} health!")
            print(f"{target.name}'s health is now {target.health}")
            print(f"{caster.name}'s mana is now {caster.mana}")
        else:
            print(f"{caster.name} does not have enough mana to cast {self.name}.")

class DarkFire(DamageSpell):
    def __init__(self) -> None:
        super().__init__("Dark Fire", "Dark", 20, 40)  # Mana cost is 20, damage is 40


class ShadowCurse(DamageSpell):
    def __init__(self) -> None:
        super().__init__("Shadow Curse", "Dark", 30, 50)  # Mana cost is 30, damage is 50


class Heal(HealingSpell):
    def __init__(self) -> None:
        super().__init__("Heal", "Light", 15, 25)  # Mana cost is 15, heals 25


class HolyLight(DamageSpell):
    def __init__(self) -> None:
        super().__init__("Holy Light", "Light", 25, 35)  # Mana cost is 25, heals 35

# List of available spells by category
dark_spells = [DarkFire(), ShadowCurse()]
light_spells = [Heal(), HolyLight()] 
