'''
Алгоритм программы
1. Вывести меню
2. Попросить пользователя ввести число и выбрать операуию (+,-,*,/,**)
3. Посчитать результат и вывести пользователю
'''

'''
# ШАГ 1. Пишем "в лоб" - чтобы работало

print('Добро пожаловить!\n\
1.Сумма\n\
2.Разница\n\
3.Произведение\n\
4.Частное\n\
5.Степень\n\
6.Выход')

user_choose = input('Введите пункт меню числом: ')

if user_choose == '1':
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    result = number1 + number2
    print(result)
elif user_choose == '2':
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    result = number1 - number2
    print(result)
elif user_choose == '3':
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    result = number1 * number2
    print(result)
elif user_choose == '4':
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    result = number1 / number2
    print(result)
elif user_choose == '5':
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    result = number1 ** number2
    print(result)
elif user_choose == '6':
    pass
else:
    print('Неверный пункт меню!')
'''

'''
# ШАГ 2. Добавляем проверки и циклы

while True:
    print('Добро пожаловить!\n\
1.Сумма\n\
2.Разница\n\
3.Произведение\n\
4.Частное\n\
5.Степень\n\
6.Выход')

    user_choose = input('Введите пункт меню числом: ')
    user_choose = int(user_choose)

    if user_choose not in range(1, 6+1):
        print('Неверный пункт меню!')
    else:
        if user_choose == 1:
            number1 = int(input('Введите первое число: '))
            number2 = int(input('Введите второе число: '))
            result = number1 + number2
            print(result)
            break
        elif user_choose == 2:
            number1 = int(input('Введите первое число: '))
            number2 = int(input('Введите второе число: '))
            result = number1 - number2
            print(result)
            break
        elif user_choose == 3:
            number1 = int(input('Введите первое число: '))
            number2 = int(input('Введите второе число: '))
            result = number1 * number2
            print(result)
            break
        elif user_choose == 4:
            number1 = int(input('Введите первое число: '))
            number2 = int(input('Введите второе число: '))
            
            if number2 == 0:
                print('Второе число равно 0!')
                continue
            
            result = number1 / number2
            print(result)
            break
        elif user_choose == 5:
            number1 = int(input('Введите первое число: '))
            number2 = int(input('Введите второе число: '))
            result = number1 ** number2
            print(result)
            break
        else:
            break
'''

'''
# ШАГ 3. Исключения

while True:
    while True:
        print('Добро пожаловить!\n\
1.Сумма\n\
2.Разница\n\
3.Произведение\n\
4.Частное\n\
5.Степень\n\
6.Выход')

        user_choose = input('Введите пункт меню числом: ')
        try:
            user_choose = int(user_choose)
            assert user_choose in range(1, 6+1)
        except AssertionError:
            print('Неверный пункт меню!')
        except:
            print('Вы ввели не число!')
        else:
            break
    
    if user_choose == 1:
        while True:
            number1 = input('Введите первое число: ')
            try:
                number1 = int(number1)
            except:
                print('Вы ввели не число!')
            else:
                number2 = input('Введите второе число: ')
                try:
                    number2 = int(number2)
                except:
                    print('Вы ввели не число!')
                else:  
                    break
        result = number1 + number2
        print(result)
        
        user_choose = input('Рассчитать другую пару, [y/n]: ')
        if user_choose == 'n':
            break
        
    elif user_choose == 2:
        number1 = int(input('Введите первое число: '))
        number2 = int(input('Введите второе число: '))
        result = number1 - number2
        print(result)
        break
    elif user_choose == 3:
        number1 = int(input('Введите первое число: '))
        number2 = int(input('Введите второе число: '))
        result = number1 * number2
        print(result)
        break
    elif user_choose == 4:
        number1 = int(input('Введите первое число: '))
        number2 = int(input('Введите второе число: '))

        if number2 == 0:
            print('Второе число равно 0!')
            continue

        result = number1 / number2
        print(result)
        break
    elif user_choose == 5:
        number1 = int(input('Введите первое число: '))
        number2 = int(input('Введите второе число: '))
        result = number1 ** number2
        print(result)
        break
    else:
        break
'''

'''
# ШАГ 4. Функции


def print_menu():
    print('Добро пожаловить!\n\
1.Сумма\n\
2.Разница\n\
3.Произведение\n\
4.Частное\n\
5.Степень\n\
6.Выход')


def get_item_menu():
    while True:
        print_menu()
        user_choose = input('Введите пункт меню числом: ')
        try:
            user_choose = int(user_choose)
            assert user_choose in range(1, 6+1)
        except AssertionError:
            print('Неверный пункт меню!')
        except:
            print('Вы ввели не число!')
        else:
            return user_choose


def get_two_numbers():
    while True:
        number1 = input('Введите первое число: ')
        try:
            number1 = int(number1)
        except:
            print('Вы ввели не число!')
        else:
            number2 = input('Введите второе число: ')
            try:
                number2 = int(number2)
            except:
                print('Вы ввели не число!')
            else:
                return number1, number2


def get_exit():
    user_choose = input('Рассчитать другую пару, [y/n]: ')
    return user_choose == 'n'


def sum_menu():
    while True:
        number1, number2 = get_two_numbers()
        result = number1 + number2
        print(result)
        if get_exit():
            break


def diff_menu():
    while True:
        number1, number2 = get_two_numbers()
        result = number1 - number2
        print(result)
        if get_exit():
            break


def mult_menu():
    while True:
        number1, number2 = get_two_numbers()
        result = number1 * number2
        print(result)
        if get_exit():
            break


def div_menu():
    while True:
        while True:
            number1, number2 = get_two_numbers()
            if number2 == 0:
                print('Второе число равно 0!')
            else:
                break
        result = number1 / number2
        print(result)
        if get_exit():
            break

def pow_menu():
    while True:
        number1, number2 = get_two_numbers()
        result = number1 ** number2
        print(result)
        if get_exit():
            break

def start():
    while True:
        user_choose = get_item_menu()
        if user_choose == 1:
            sum_menu()
        elif user_choose == 2:
            diff_menu()
        elif user_choose == 3:
            mult_menu()
        elif user_choose == 4:
            div_menu()
        elif user_choose == 5:
            pow_menu()
        else:
            break

start()
'''

'''
# ШАГ 5. Рефакторинг


def print_menu():
    print('Добро пожаловить!\n\
1.Сумма\n\
2.Разница\n\
3.Произведение\n\
4.Частное\n\
5.Степень\n\
6.Выход')


def get_int(msg: str, err_type_msg='Вы ввели не число!') -> int:
    """Функция, которая просит ввести целое число

    Args:
        msg (str): сообщение для пользователя
        err_type_msg (str, optional): текст ошибки. Defaults to 'Вы ввели не число!'.

    Returns:
        int: введенное число
    """
    while True:
        user_choose = input(f'{msg}: ')
        try:
            user_choose = int(user_choose)
        except:
            print(err_type_msg)
        else:
            return user_choose


def get_item_menu():
    while True:
        print_menu()
        user_choose = get_int('Введите пункт меню числом')
        try:
            assert user_choose in range(1, 6+1)
        except AssertionError:
            print('Неверный пункт меню!')
        else:
            return user_choose


def get_two_numbers():
    number1 = get_int('Введите первое число')
    number2 = get_int('Введите второе число')
    return number1, number2


def get_exit(result: int):
    print(result)
    return input('Рассчитать другую пару, [y/n]: ') == 'n'


def sum_menu():
    while True:
        number1, number2 = get_two_numbers()
        result = number1 + number2
        if get_exit(result):
            break


def diff_menu():
    while True:
        number1, number2 = get_two_numbers()
        result = number1 - number2
        if get_exit(result):
            break


def mult_menu():
    while True:
        number1, number2 = get_two_numbers()
        result = number1 * number2
        if get_exit(result):
            break


def div_menu():
    while True:
        while True:
            number1, number2 = get_two_numbers()
            if number2 == 0:
                print('Второе число равно 0!')
            else:
                break
        result = number1 / number2
        if get_exit(result):
            break


def pow_menu():
    while True:
        number1, number2 = get_two_numbers()
        result = number1 ** number2
        if get_exit(result):
            break


def start():
    while True:
        user_choose = get_item_menu()
        if user_choose == 1:
            sum_menu()
        elif user_choose == 2:
            diff_menu()
        elif user_choose == 3:
            mult_menu()
        elif user_choose == 4:
            div_menu()
        elif user_choose == 5:
            pow_menu()
        else:
            break


start()
'''
# ШАГ 5. Рефакторинг (сложнее)


def print_menu():
    print('Добро пожаловить!\n\
1.Сумма\n\
2.Разница\n\
3.Произведение\n\
4.Частное\n\
5.Степень\n\
6.Выход')


def get_int(msg: str, err_type_msg='Вы ввели не число!') -> int:
    """Функция, которая просит ввести целое число

    Args:
        msg (str): сообщение для пользователя
        err_type_msg (str, optional): текст ошибки. Defaults to 'Вы ввели не число!'.

    Returns:
        int: введенное число
    """
    while True:
        user_choose = input(f'{msg}: ')
        try:
            user_choose = int(user_choose)
        except:
            print(err_type_msg)
        else:
            return user_choose


def get_item_menu():
    while True:
        print_menu()
        user_choose = get_int('Введите пункт меню числом')
        try:
            assert user_choose in range(1, 6+1)
        except AssertionError:
            print('Неверный пункт меню!')
        else:
            return user_choose


def get_two_numbers():
    number1 = get_int('Введите первое число')
    number2 = get_int('Введите второе число')
    return number1, number2


def get_exit(result: int):
    print(result)
    return input('Рассчитать другую пару, [y/n]: ') == 'n'


def operation_action(func):
    while True:
        number1, number2 = get_two_numbers()
        result = func(number1, number2)
        if result == None:
            continue
        if get_exit(result):
            break


def div_menu():
    def check_number2(number1: int, number2: int):
        if number2 == 0:
            print('Второе число равно 0!')
        else:
            return number1 / number2
        return None

    operation_action(check_number2)


def start():
    while True:
        user_choose = get_item_menu()
        if user_choose == 1:
            operation_action(lambda i, j: i+j)
        elif user_choose == 2:
            operation_action(lambda i, j: i-j)
        elif user_choose == 3:
            operation_action(lambda i, j: i*j)
        elif user_choose == 4:
            div_menu()
        elif user_choose == 5:
            operation_action(lambda i, j: i**j)
        else:
            break


start()
