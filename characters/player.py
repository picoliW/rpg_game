class Player:
    def __init__(self, name, health, attackdamage, mana):
        self.name = name
        self.health = health
        self.attackdamage = attackdamage
        self.mana = mana

    def attack(self, target):
        target.health -= self.damage

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Damage per attack: {self.attackdamage}, Mana {self.mana}"

player_instance = Player("player_name", 100, 30, 50)

