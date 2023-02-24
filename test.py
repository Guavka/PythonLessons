# Шаг 3. Исключения и зацикливание
menu_dict = {
    'coffee': {
        '350ml': 300,
        '400ml': 400
    },
    'tea': {
        '400ml': 300
    }
}

while True:
    menu_list = list(menu_dict.keys())
    exit_index = len(menu_list)+1

    while True:
        for i in range(len(menu_list)):
            print(f'{i+1}.{menu_list[i].capitalize()}')
        print(f'{i+2}.Exit')

        user_choose = input('Input menu index: ')
        try:
            user_choose = int(user_choose)
            assert user_choose in range(1, exit_index+1)
        except ValueError:
            print('You input not a number!')
        except AssertionError:
            print(f'Index must be in range [1, {exit_index}]')
        else:
            break

    if user_choose == exit_index:
        break
    drink_name = menu_list[user_choose-1]
    size_dict = menu_dict[drink_name]

    size_list = list(size_dict.keys())
    exit_index = len(size_list)+1

    while True:
        for i in range(len(size_list)):
            print(f'{i+1}.{size_list[i].capitalize()}')
        print(f'{i+2}.Exit')

        user_choose = input('Input menu index: ')
        try:
            user_choose = int(user_choose)
            assert user_choose in range(1, exit_index+1)
        except ValueError:
            print('You input not a number!')
        except AssertionError:
            print(f'Index must be in range [1, {exit_index}]')
        else:
            break

    if user_choose == exit_index:
        break

    drink_size = size_list[user_choose-1]
    price = size_dict[drink_size]

    print(drink_name, drink_size, price)