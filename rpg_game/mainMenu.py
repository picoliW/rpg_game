from characters.player import player_instance
from fight import fight
from characters.practice import practice
from characters.options import options
from store.armor_store import armor

def menu():
    print('-------------------Welcome to the RPG--------------------')
    player_name = input('Please type your name: ')
    player_instance.name = player_name

    print("Your character stats: ", player_instance)

    player_choose = input('What you want to do? \n 1- Fight \n 2- Practice \n 3- Store \n 4- Options \n')
   
    match player_choose:
        case '1':
            fight()
        case '2':
            practice()
        case '3':
            armor()
        case '4':
            options()
    

menu()
