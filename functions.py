from character import Mage, Warrior, Cleric

def choose_class():
    available_classes = ["Warrior", "Mage", "Cleric"]
    print("Choose your class:")
    for i, class_name in enumerate(available_classes, 1):
        print(f"{i}. {class_name}")
    
    choice = int(input("Enter the number of your chosen class: ")) - 1
    return available_classes[choice]

def create_character():
    character_name = input("Enter Your Name: ")
    chosen_class = choose_class()

    if chosen_class == "Warrior":
        return Warrior(character_name,100)
    elif chosen_class == "Mage":
        return Mage(character_name, 60, 100)
    elif chosen_class == "Cleric":
        return Cleric(character_name)
