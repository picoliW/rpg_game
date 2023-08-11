from characters.player import player_instance
from fight import fight
from characters.practice import practice
from characters.options import options
from store.store import store

def menu():
    print('-------------------Welcome to the RPG--------------------')
    print('You are a simple villager born in distant lands who knows a few spells.')
    print('Fight the monsters and kill the demon lord to save your world.')
    player_name = input('Please type your Hero name: ')
    player_instance.name = player_name

    print("Your Hero stats: ", player_instance)

    player_choose = input('What you want to do? \n 1- Fight \n 2- Practice \n 3- Store \n 4- Options \n')
   
    match player_choose:
        case '1':
            fight()
        case '2':
            practice()
        case '3':
            store()
        case '4':
            options()
    

menu()
