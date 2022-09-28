from utils import get_data, print_data


def start_game():
    user_name = get_data('Input user name: ')
    print_data(f'Username: {user_name}')
