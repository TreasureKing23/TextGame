from functions import *
from character import *
from spell import *

# Start the game and create the player character
player = create_character()

print(f"\nWelcome, {player.name} the {player.__class__.__name__}!")
print(f"Your starting health is {player.health}")
if hasattr(player, 'mana'):
    print(f"Your starting mana is {player.mana}")

# Create an enemy character (for example purposes)
enemy = create_character()  # Creating a new character as the enemy
print(f"\nYour enemy is {enemy.name} the {enemy.__class__.__name__}!")
print(f"The enemy's starting health is {enemy.health}")
if hasattr(enemy, 'mana'):
    print(f"The enemy's starting mana is {enemy.mana}")

# Main game loop
while player.health > 0 and enemy.health > 0:
    print("\nWhat would you like to do?")
    print("1. Attack")
    print("2. Cast Spell")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Attack logic: player attacks enemy
        player.attack(enemy)
        print(f"You attack {enemy.name}. {enemy.name}'s health is now {enemy.health}.")

        # Check if the enemy is defeated
        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!")
            break

    elif choice == "2":
        # Cast Spell
        if hasattr(player, 'spells') and player.spells:
            print("\nChoose a spell to cast:")
            for i, spell in enumerate(player.spells, 1):
                print(f"{i}. {spell.name} (Mana Cost: {spell.mana_cost})")

            spell_choice = int(input("Enter the number of the spell you want to cast: ")) - 1
            if 0 <= spell_choice < len(player.spells):
                selected_spell = player.spells[spell_choice]
                
                # Determine the target based on spell type
                if isinstance(selected_spell, HealingSpell):
                    selected_spell.cast(player, player)  # Heal self
                elif isinstance(selected_spell, DamageSpell):
                    selected_spell.cast(player, enemy)  # Attack enemy
                    print(f"{enemy.name}'s health is now {enemy.health}.")
                    
                # Check if the enemy is defeated after the spell cast
                if enemy.health <= 0:
                    print(f"{enemy.name} has been defeated!")
                    break
            else:
                print("Invalid choice!")
        else:
            print("Your character has no spells to cast.")

    elif choice == "3":
        print("Quitting the game.")
        break

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

    # Enemy turn logic can go here if needed (optional)

# End game message
if player.health <= 0:
    print("You have been defeated!")
elif enemy.health <= 0:
    print("Congratulations, you have defeated the enemy!")
