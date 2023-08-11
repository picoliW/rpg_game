class Player:
    def __init__(self, name, health, damage, mana, gold):
        self.name = name
        self.health = health
        self.damage = damage
        self.mana = mana
        self.gold = gold

    def attack(self, target):
        target.health -= self.damage

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Damage per attack: {self.damage}, Mana {self.mana}, Gold {self.gold}"

player_instance = Player("player_name", 100, 30, 50, 500)

