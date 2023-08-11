from characters.player import player_instance

def options():
    option_select = input('1- Change name\n')
    if option_select == '1':
        new_name = input('Type your new name: ')
        player_instance.name = new_name
        print(f'Name sucessfully changed your new name{player_instance.name}')





