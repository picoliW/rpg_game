from characters.player import player_instance
from fight import fight
from characters.practice import practice
from characters.options import options

def menu():
    print('-------------------Welcome to the RPG--------------------')
    player_name = input('Please type your name: ')
    player_instance.name = player_name

    print("Your character stats: ", player_instance)

    player_choose = input('What you want to do? \n 1- fight \n 2- practice \n 3- options \n')
   
    match player_choose:
        case '1':
            fight()
        case '2':
            practice()
        case '3':
            options()
    

menu()
