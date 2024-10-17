# main.py
from functions import create_character

# Start the game
player = create_character()

print(f"\nWelcome, {player.name} the {player.__class__.__name__}!")
print(f"Your starting health is {player.health}")
if hasattr(player, 'mana'):
    print(f"Your starting mana is {player.mana}")



player.cast_spell("Dark Fire", player)

player.cast_spell("Shadow Curse", player)

player.cast_spell("Heal", player)
