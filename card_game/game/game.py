from utils.console import get_data_infinite, print_data
from user.user import User


def game():
    def round(user: User):
        def get_bet():
            while True:
                try:
                    bet = get_data_infinite('Input bet:')
                    assert bet <= user.money and bet > 0, 'Incorrect bet'
                except AssertionError as ex:
                    print_data(ex)
                else:
                    break

        def get_number():
            while True:
                try:
                    user_choose = get_data_infinite('Input number:')
                    assert user_choose >= 0 and user_choose <= 3, 'Incorrect number'
                except AssertionError as ex:
                    print_data(ex)
                else:
                    break

        from random import randint

        bet = get_bet()
        user.money -= bet
        random_number = randint(0, 3)
        user_choose = get_number()

        if random_number == user_choose:
            print_data('Win!')
            user.money += bet*2
        else:
            print_data('Loose!')

        user_choose = get_data_infinite('Try again?[y/n]', str)
        return user_choose.lower() == 'n'

    print('Game started')
    user_name = get_data_infinite('Input name:', str)
    user_money = get_data_infinite('Input money:')

    user = User(user_name, user_money)

    while round(user=user):
        pass
