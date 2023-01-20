from scripts.game.game_controller import start_game


def start_menu():
    while True:
        print('Welcome!\n Choose item menu:')
        user_choose = input('1.Start game\n2.Exit')

        if user_choose == 1:
            start_game()
        elif user_choose == 2:
            break
        else:
            print('Incorrect menu item!')


def get_player():
    from models.players.player import Player
    while True:
        user_name = input('Input name: ')
        user_money = input('Input money: ')

        try:
            return Player(user_name, user_money)
        except Exception as ex:
            print(ex)
