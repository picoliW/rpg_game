from store.armor_store import armor
from store.sword_store import sword

def store():
    print('Welcome to the store!')
    store_selection = input('Select the section:\n 1- Armor store \n 2- Sword store')
    
    if store_selection == '1':
        armor()
    elif store_selection == '2':
        sword()
