from characters.player import player_instance
from enemies.goblin import goblin_instance
from enemies.dragon import dragon_instance
from characters.magic import fireball, thunderbolt, ice_spike
from characters.armor import leather_armor, plate_armor, magic_robes 

def fight():
    while True:
        print("Player:", player_instance)
        print("Goblin:", goblin_instance)
        print("Dragon:", dragon_instance)

        action = input("Enter an action \n1- Sword Attack \n 2- Magic attack \n 3- Run \n ")
        match action:
            case "1":
                player_instance.attack(goblin_instance)
                player_instance.attack(dragon_instance)
                goblin_instance.attack(player_instance)
                dragon_instance.attack(player_instance)
                if player_instance.health <= 0:
                    print('Game Over')
                    break
                if goblin_instance.health <= 0:
                    player_instance.gold += 20
                    print('You killed a goblin! +20 gold')
                    goblin_instance.health = 50
                    fight()
            case "2":
                print("Choose a magic skill:")
                print("1- Fireball (20 DMG)(Cost 10 Mana)")
                print("2- Thunderbolt (25 DMG)(Cost 13 Mana)")
                print("3- Ice Spike (15 DMG)(MultiTarget)(Cost 15 Mana)")
                magic_choice = input("Select a magic skill: ")

                if magic_choice == '1':
                    if player_instance.mana <= 10:
                        print('You dont have enough mana')
                        fight()
                    else:
                        magic_target = input('what target? (goblin/dragon)')
                        player_instance.mana -= 10
                        if magic_target == 'goblin':
                            fireball.cast(goblin_instance)
                            goblin_instance.attack(player_instance)
                            dragon_instance.attack(player_instance)
                            if goblin_instance.health <= 0:
                                player_instance.gold += 20
                                print('You killed a goblin! +20 gold')
                                goblin_instance.health = 50
                                fight()
                        elif magic_target == 'dragon':
                            fireball.cast(dragon_instance)
                            goblin_instance.attack(player_instance)
                            dragon_instance.attack(player_instance)
                            if dragon_instance.health <= 0:
                                player_instance.gold += 40
                                print('You killed a dragon! +40 gold')
                                dragon_instance.health = 200
                                fight()

                elif magic_choice == '2':
                    if player_instance.mana <= 13:
                        print('You dont have enough mana')
                        fight()
                    else:
                        player_instance.mana -= 13
                        magic_target = input('what target? (goblin/dragon)')
                        if magic_target == 'goblin':
                            thunderbolt.cast(goblin_instance)
                            goblin_instance.attack(player_instance)
                            dragon_instance.attack(player_instance)
                            if goblin_instance.health <= 0:
                                player_instance.gold += 20
                                print('You killed a goblin! +20 gold')
                                goblin_instance.health = 50
                                fight()
                        elif magic_target == 'dragon':
                            thunderbolt.cast(dragon_instance)
                            goblin_instance.attack(player_instance)
                            dragon_instance.attack(player_instance)
                            if dragon_instance.health <= 0:
                                player_instance.gold += 40
                                print('You killed a dragon! +40 gold')
                                dragon_instance.health = 200
                                fight()

                elif magic_choice == '3':
                    if player_instance.mana <= 15:
                        print('You dont have enough mana')
                        fight()
                    else:
                        player_instance.mana -= 15
                        ice_spike.cast(goblin_instance)
                        ice_spike.cast(dragon_instance)
                        goblin_instance.attack(player_instance)
                        dragon_instance.attack(player_instance)
                        if goblin_instance.health <= 0:
                            player_instance.gold += 20
                            print('You killed a goblin! +20 gold')
                            goblin_instance.health = 50
                            fight()
                        if dragon_instance.health <= 0:
                            player_instance.gold += 40
                            print('You killed a dragon! +40 gold')
                            dragon_instance.health = 200
                            fight()
                              
                else:
                    print("Invalid choice.")
                    fight()
 
            case "3":
                break 

if __name__ == "__main__":
    fight()
