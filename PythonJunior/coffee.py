'''
Кофемашина
1. Выводим меню
2. Выбираем напиток
3. Выбираем объем
4. Печатаем чек
'''

'''
# ШАГ 1. Кодим "в лоб"

drink1_name = 'Coffee'

drink1_volume1 = '350ml'
drink1_volume1_price = 300

drink1_volume2 = '400ml'
drink1_volume2_price = 400

drink2_name = 'Tea'

drink2_volume1 = '400ml'
drink2_volume1_price = 400

while True:
    print('Welcome!')
    user_choose = input(f'1.{drink1_name}\n2.{drink2_name}\n3.Exit\n')

    if user_choose == '1':
        print(f'You choose {drink1_name}:\n\
1.{drink1_volume1}: {drink1_volume1_price}\n\
2.{drink1_volume2}: {drink1_volume2_price}\n\
3.Exit')        
        user_choose = input('Input menu item index: ')
        
        if user_choose == '1':
            print(f'{drink1_name} {drink1_volume1} {drink1_volume1_price}')
        elif user_choose == '2':
            print(f'{drink1_name} {drink1_volume2} {drink1_volume2_price}')
        elif user_choose == '3':
            break
        else:
            print('Error menu item!')        
    elif user_choose == '2':
        print(f'You choose {drink2_name}:\n\
1.{drink2_volume1}: {drink2_volume1_price}\n\
2.Exit')     
        if user_choose == '1':
            print(f'{drink2_name} {drink2_volume1} {drink2_volume1_price}')
        elif user_choose == '2':
            break
        else:
            print('Error menu item!')
    elif user_choose == '3':
        break
    else:
        print('Error menu item!')
'''

'''
# Шаг 2. Переходим на словари
menu_dict = {
    'coffee': {
        '350ml': 300,
        '400ml': 400
    },
    'tea': {
        '400ml': 300,
        '340ml': 250
    }
}

while True:
    menu_list = list(menu_dict.keys())

    for i in range(len(menu_list)):
        print(f'{i+1}.{menu_list[i].capitalize()}')
    print(f'{i+2}.Exit')

    user_choose = input('Input menu index: ')
    user_choose = int(user_choose)

    exit_index = len(menu_list)+1
    if user_choose not in range(1, exit_index+1):
        print(f'Index must be in range [1, {exit_index}]')
    else:
        if user_choose == exit_index:
            break

        drink_name = menu_list[user_choose-1]
        size_dict = menu_dict[drink_name]

        size_list = list(size_dict.keys())

        for i in range(len(size_list)):
            print(f'{i+1}.{size_list[i].capitalize()}')
        print(f'{i+2}.Exit')

        user_choose = input('Input menu index: ')
        user_choose = int(user_choose)

        exit_index = len(size_list)+1
        if user_choose not in range(1, exit_index+1):
            print(f'Index must be in range [1, {exit_index}]')
        else:
            if user_choose == exit_index:
                break

            drink_size = size_list[user_choose-1]
            price = size_dict[drink_size]

            print(drink_name, drink_size, price)
'''

'''
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
'''

'''
# Шаг 4. Функции
def main():
    menu_dict = {
        'coffee': {
            '350ml': 300,
            '400ml': 400
        },
        'tea': {
            '400ml': 300
        }
    }

    def print_menu(menu_list):
        for i in range(len(menu_list)):
            print(f'{i+1}.{menu_list[i].capitalize()}')
        print(f'{i+2}.Exit')

    def get_menu_index(menu_list, exit_index):
        while True:
            print_menu(menu_list)

            user_choose = input('Input menu index: ')
            try:
                user_choose = int(user_choose)
                assert user_choose in range(1, exit_index+1)
            except ValueError:
                print('You input not a number!')
            except AssertionError:
                print(f'Index must be in range [1, {exit_index}]')
            else:
                if user_choose == exit_index:
                    raise SystemExit                
                return user_choose

    def get_drink():
        menu_list = list(menu_dict.keys())
        exit_index = len(menu_list)+1

        user_choose = get_menu_index(menu_list, exit_index)

        drink_name = menu_list[user_choose-1]
        size_dict = menu_dict[drink_name]
        
        return drink_name, size_dict

    def get_size():
        size_list = list(size_dict.keys())
        exit_index = len(size_list)+1

        user_choose = get_menu_index(size_list, exit_index)

        drink_size = size_list[user_choose-1]
        price = size_dict[drink_size]
        
        return drink_size, price

    while True:
        drink_name, size_dict = get_drink()
        drink_size, price = get_size()        

        print(drink_name.capitalize(), drink_size, price)


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        print('Good day!')
'''

'''
# Шаг 5. Рефакторинг
def main():
    menu_dict = {
        'coffee': {
            '350ml': 300,
            '400ml': 400
        },
        'tea': {
            '400ml': 300
        }
    }

    def print_menu(menu_list):
        for i in range(len(menu_list)):
            print(f'{i+1}.{menu_list[i].capitalize()}')
        print(f'{i+2}.Exit')

    def get_menu_index(menu_list, exit_index):
        def get_int_range():            
            while True:
                print_menu(menu_list)

                user_choose = input('Input menu index: ')
                try:
                    user_choose = int(user_choose)
                    assert user_choose in range(1, exit_index+1)
                except ValueError:
                    print('You input not a number!')
                except AssertionError:
                    print(f'Index must be in range [1, {exit_index}]')
                else:
                    return user_choose
                
        user_choose = get_int_range() 
        if user_choose == exit_index:
            raise SystemExit                
        return user_choose

    def get_key_value(data_dict:dict):
        data_list = list(data_dict.keys())
        exit_index = len(data_list)+1

        user_choose = get_menu_index(data_list, exit_index)

        key = data_list[user_choose-1]
        value = data_dict[key]
        
        return key, value

    while True:
        drink_name, size_dict = get_key_value(menu_dict)
        drink_size, price = get_key_value(size_dict)        

        print(drink_name.capitalize(), drink_size, price)


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        print('Good day!')
'''

# Шаг 6. Автоматизация - отделение данных от логики


def main():
    menu_dict = {
        'drink': {
            'coffee': {
                '350ml': 300,
                '400ml': 400
            },
            'tea': {
                '400ml': 300
            }
        },
        'snack': {
            'chips': {
                'small': 120
            }
        }
    }

    print_names = ['Category', 'Name', 'Size', 'Price']

    def print_menu(menu_list):
        for i in range(len(menu_list)):
            print(f'{i+1}.{menu_list[i].capitalize()}')
        print(f'{i+2}.Exit')

    def get_menu_index(menu_list, exit_index):
        def get_int_range():
            while True:
                print_menu(menu_list)

                user_choose = input('Input menu index: ')
                try:
                    user_choose = int(user_choose)
                    assert user_choose in range(1, exit_index+1)
                except ValueError:
                    print('You input not a number!')
                except AssertionError:
                    print(f'Index must be in range [1, {exit_index}]')
                else:
                    return user_choose

        user_choose = get_int_range()
        if user_choose == exit_index:
            raise SystemExit
        return user_choose

    def get_key_value(data_dict: dict):
        data_list = list(data_dict.keys())
        exit_index = len(data_list)+1

        user_choose = get_menu_index(data_list, exit_index)

        key = data_list[user_choose-1]
        value = data_dict[key]

        return key, value

    while True:
        result_list = []
        data_dict = menu_dict
        while True:
            key, value = get_key_value(data_dict)

            result_list.append(key.capitalize())
            data_dict = value

            if type(value) is not dict:
                result_list.append(value)
                break

        print('---------------')
        for i in range(len(print_names)):
            print(f'{print_names[i]}: {result_list[i]}')
        print('---------------')


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        print('Good day!')
