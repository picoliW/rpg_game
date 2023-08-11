class MagicSkill:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def cast(self, target):
        print(f"Casting {self.name} on {target.name}!")
        target.health -= self.damage

fireball = MagicSkill("Fireball", 20)
thunderbolt = MagicSkill("Thunderbolt", 25)
ice_spike = MagicSkill("Ice Spike", 15)
