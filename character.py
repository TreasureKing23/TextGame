from weapon import hands
from spell import *
class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

        #self.weapon = hands

    # def attack (self, target)-> None:
    #     target.health -= self.weapon.damage
    #     target.health =max(target.health, 0)

    def cast_spell(self, spell_name: str, target) -> None:
        # Magic classes should have mana
        if not hasattr(self, "mana"):
            print(f"{self.name} cannot cast spells!")
            return

        # Find the spell in the character's spell list
        spell = next((spell for spell in self.spells if spell.name == spell_name), None)
        if spell:
            spell.cast(self, target)
        else:
            print(f"{self.name} does not know the spell {spell_name}.")
    

class Warrior(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name, 100,)
       


class Mage(Character):
    def __init__(self, name: str, health: int, mana: int = 100) -> None:
        super().__init__(name, 60)
        self.mana = mana  # Mana for spell casting
        self.spells = dark_spells  # Load dark spells
      


# Cleric class that loads light spells and has mana
class Cleric(Character):
    def __init__(self, name: str, health: int, mana: int = 100) -> None:
        super().__init__(name, 75)
        self.mana = mana  # Mana for spell casting
        self.spells = light_spells  # Load light spells


# class Ranger(Character):
#     def __init__(self, name: str, health: int) -> None:
#         super().__init__(name, health,)


available_classes = ["Warrior", "Mage", "Cleric"]