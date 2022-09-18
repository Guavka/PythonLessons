from .game import game

def start_menu():
    while True:
        print('Welcome to game!\nChoose menu item:\n1.Start\n2.Exit')
        user_choose = input()
        if user_choose == '1':
            game()
        elif user_choose == '2':
            break
        else:
            print('Error! Choose 1 or 2')
