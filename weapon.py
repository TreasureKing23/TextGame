class Weapon:
    def __init__(self, name: str, damage: int) -> None:
        self.name = name
        self.damage = damage


sword = Weapon("Sword", 10)

staff = Weapon("Staff", 5)     

mace = Weapon("Mace", 7)

hands = Weapon("Deez Hands", 1)