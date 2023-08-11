class Armor:
    def __init__(self, name, defense, cost):
        self.name = name
        self.defense = defense
        self.cost = cost

    def apply_armor(self, target):
        print(f"Applying {self.name} to {target.name}!")
        target.defense += self.defense

leather_armor = Armor("Leather Armor", 4, 40)
plate_armor = Armor("Plate Armor", 10, 60)
magic_robes = Armor("Magic Robes", 3, 50)
