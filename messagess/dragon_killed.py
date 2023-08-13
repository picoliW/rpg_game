from enemies.dragon import dragon_instance
from characters.player import player_instance

def dragon_killed():
    if dragon_instance.health <= 0:
        player_instance.gold += 90
        print('You killed a dragon! +90 gold')
        dragon_instance.health = 150
        dragon_instance.armor = 50