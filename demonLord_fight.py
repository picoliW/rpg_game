from characters.player import player_instance
from enemies.demon_lord import demonlord_instance
from characters.magic import fireball, thunderbolt, ice_spike


def demonLord_fight():
    while True:
        print('-------------------Demon Lord Fight--------------------')
        while player_instance.health > 0:
            print("Player:", player_instance)
            print("Demon Lord:", demonlord_instance)
            

            action = input("Enter an action \n1- Sword Attack \n 2- Magic attack \n 3- Run \n ")
            match action:
                case "1":
                    player_instance.attack(demonlord_instance)
                    demonlord_instance.attack(player_instance)
                    if demonlord_instance.health <= 0:
                        player_instance.gold += 1000
                        print('You killed the Demon Lord! +1000 gold')
                        demonLord_fight()
                case "2":
                    print("Choose a magic skill:")
                    print(f"1- {fireball.name} (Damage: {fireball.damage}) (Mana cost: {fireball.manacost})")
                    print(f"2- {thunderbolt.name} (Damage: {thunderbolt.damage}) (Mana cost: {thunderbolt.manacost})")
                    print(f"3- {ice_spike.name} (Damage: {ice_spike.damage}) (Mana cost: {ice_spike.manacost})")
                    magic_choice = input("Select a magic skill: ")

                    if magic_choice == '1':
                        if player_instance.mana < fireball.manacost:
                            print('You dont have enough mana')
                            demonLord_fight()
                        else:
                            player_instance.mana -= fireball.manacost
                            fireball.cast(demonlord_instance)
                            demonlord_instance.attack(player_instance)
                            if demonlord_instance.health <= 0:
                                    player_instance.gold += 1000
                                    print('You killed the Demon Lord! +1000 gold')
                                    demonLord_fight()

                    elif magic_choice == '2':
                        if player_instance.mana < thunderbolt.manacost:
                            print('You dont have enough mana')
                            demonLord_fight()
                        else:
                            player_instance.mana -= thunderbolt.manacost
                            thunderbolt.cast(demonlord_instance)
                            demonlord_instance.attack(player_instance)
                            if demonlord_instance.health <= 0:
                                    player_instance.gold += 1000
                                    print('You killed the Demon Lord! +1000 gold')
                                    demonLord_fight()

                    elif magic_choice == '3':
                        if player_instance.mana < ice_spike.manacost:
                            print('You dont have enough mana')
                            demonLord_fight()
                        else:
                            player_instance.mana -= ice_spike.manacost
                            ice_spike.cast(demonlord_instance)
                            demonlord_instance.attack(player_instance)
                            if demonlord_instance.health <= 0:
                                player_instance.gold += 1000
                                print('You killed the Demon Lord +1000 gold')
                                demonLord_fight()                            
                    else:
                        print("Invalid choice.")
                        demonLord_fight()

        else:                       
            print('Game Over')
            break

