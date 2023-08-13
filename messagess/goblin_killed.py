from enemies.goblin import goblin_instance
from characters.player import player_instance

def goblin_killed():
    if goblin_instance.health <= 0:
        player_instance.gold += 20
        print('You killed a goblin! +20 gold')
        goblin_instance.health = 40
        goblin_instance.armor = 10
