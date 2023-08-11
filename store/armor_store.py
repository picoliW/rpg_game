from characters.player import player_instance

armor_type = ['Leather Armor', 'Plate Armor', 'Magic Robes']

def armor():
    print(f'your gold {player_instance.gold}')
    print(f'Armor available: {armor_type}')
    buy_armor = input('Do you want to buy an armor? (y/n)')
    if buy_armor == 'y':
        buy_armor_type = input('Which one do you want to buy?\n 1- Leather Armor(4 Defense)(Cost 40)\n 2- Plate Armor(10 Defense)(Cost 60)\n 3- Magic Robes(3 Defense)(Cost 50)')
        if buy_armor_type == '1':
            if player_instance.gold <= 40:
                print('You dont have enough gold')
            else:
                print('You bought Leather Armor for 40 gold')
                player_instance.gold -= 40

        if buy_armor_type == '2':
            if player_instance.gold <= 60:
                print('You dont have enough gold')
            else:
                print('You bought Plate Armor for 60 gold')
                player_instance.gold -= 60

        if buy_armor_type == '3':
            if player_instance.gold <= 50:
                print('You dont have enough gold')
            else:
                print('You bought Magic Robes for 50 gold')
                player_instance.gold -= 50
        

