from characters.player import player_instance

def practice():
    practice_stat = input('What do you want to practice? \n 1- health \n 2- damage \n 3- intelligence(Mana) \n')

    if practice_stat == '1':
        practice_task = input('Que ano foi a independencia do Brasil? ')
        if practice_task == '1822':
            player_instance.health += 10
            print(f"Your health has increased +10 your stats: {player_instance}")
            continue_practice = input('Do you want to practice again?')
            if continue_practice == 'yes':
                practice()
        else:
            print("Incorrect answer. Keep practicing!")
            practice()

    if practice_stat == '2':
        practice_task = input('How much is 50+14? ')
        if practice_task == '2':
            player_instance.damage += 7
            print(f"Your damage has increased +5 {player_instance}")
            continue_practice = input('Do you want to practice again?')
            if continue_practice == 'yes':
                practice()
    if practice_stat == '3':
        practice_task = input('What is the capital of australia? ')
        if practice_task == 'canberra':
            player_instance.mana += 6
            print(f"Your mana has increased +6 {player_instance}")
            continue_practice = input('Do you want to practice again?')
            if continue_practice == 'yes':
                practice()
        else:
            print("Incorrect answer. Keep practicing!")
            practice()
    else:
        print('Please type 1 or 2 (health/damage)')