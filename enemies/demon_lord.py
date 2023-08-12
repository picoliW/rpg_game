class Demon_lord:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        target.health -= self.damage

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Damage: {self.damage}"

demonlord_instance = Demon_lord("Demon Lord", 700, 50)