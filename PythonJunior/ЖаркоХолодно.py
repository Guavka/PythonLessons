'''
# 1. Core logic

import random

left_edge = 1
right_edge = 5
random_number = random.randint(left_edge, right_edge)

user_number = 3

if user_number == random_number:
    print('Win!!')
else:
    print('Loose')
'''

'''
# 2. Попытки

import random

left_edge = 1
right_edge = 5
tries = 3
random_number = random.randint(left_edge, right_edge)

user_number = 3

for number_try in range(tries):
    if user_number == random_number:
        print('Win!!')
    else:
        print('Loose')
'''
'''
# 3. Пользовательский ввод

import random

left_edge = input('Введите левую границу: ')
right_edge = input('Введите правую границу: ')
tries = input('Введите количество попыток: ')

left_edge = int(left_edge)
right_edge = int(right_edge)
tries = int(tries)

random_number = random.randint(left_edge, right_edge)

for number_try in range(tries):
    user_number = input('Введите число: ')
    user_number = int(user_number)
    if user_number == random_number:
        print('Угадал!!')
        break
    else:
        print('Не угадал')
else:
    print('Попытки закончились. Игра окончена')
'''

''' 
# 4. Проверки входных данных

import random

left_edge = input('Введите левую границу: ')
right_edge = input('Введите правую границу: ')
tries = input('Введите количество попыток: ')

left_edge = int(left_edge)
right_edge = int(right_edge)
tries = int(tries)

if right_edge <= left_edge:
    print('Значения границ неверны!')
else:
    if tries >= right_edge-left_edge:
        print('Попыток слишком много!')
    else:
        random_number = random.randint(left_edge, right_edge)

        for number_try in range(tries):
            user_number = input('Введите число: ')
            user_number = int(user_number)
            
            if user_number < left_edge or user_number>right_edge:
                print(f'Ошибка, число должно быть в диапазоне от [{left_edge},{right_edge}]')
            else:
                if user_number == random_number:
                    print('Угадал!!')
                    break
                else:
                    print('Не угадал')
        else:
            print('Попытки закончились. Игра окончена')
'''
''' 
# 4. Зацикливам ввод данных

import random

while True:
    left_edge = input('Введите левую границу: ')
    right_edge = input('Введите правую границу: ')

    left_edge = int(left_edge)
    right_edge = int(right_edge)

    if right_edge <= left_edge:
        print('Значения границ неверны!')
    else:        
        tries = input('Введите количество попыток: ')        
        tries = int(tries)
        if tries >= right_edge-left_edge:
            print('Попыток слишком много!')
        else:
            break
                       
        
random_number = random.randint(left_edge, right_edge)

for number_try in range(tries):
    while True:
        user_number = input('Введите число: ')
        user_number = int(user_number)
        
        if user_number < left_edge or user_number>right_edge:
            print(f'Ошибка, число должно быть в диапазоне от [{left_edge},{right_edge}]')
        else:
            break
    if user_number == random_number:
        print('Угадал!!')
        break
    else:
        print('Не угадал')
else:
    print('Попытки закончились. Игра окончена')
'''

'''
# 5. Исключения
import random

while True:
    left_edge = input('Введите левую границу: ')
    right_edge = input('Введите правую границу: ')
    tries = input('Введите количество попыток: ')
    try:
        left_edge = int(left_edge)
        right_edge = int(right_edge)        
        tries = int(tries)
        
        assert right_edge > left_edge, 'Значения границ неверны!'
        assert tries < right_edge-left_edge, 'Попыток слишком много!'
    except AssertionError as ex:
        print(ex)
    except ValueError:
        print('Введите число цифрами!')
    except Exception as ex:
        print(ex)
    else:
        break

random_number = random.randint(left_edge, right_edge)

for number_try in range(tries):
    while True:
        user_number = input('Введите число: ')        

        try:
            user_number = int(user_number)
            assert not (user_number < left_edge or
                        user_number > right_edge), f'Ошибка, число должно быть в диапазоне от [{left_edge},{right_edge}]'
        except AssertionError as ex:
            print(ex)
        except ValueError:
            print('Введите число цифрами!')
        else:
            break
    if user_number == random_number:
        print('Угадал!!')
        break
    else:
        print('Не угадал')
else:
    print('Попытки закончились. Игра окончена')
'''

# 6. Функции
import random

def get_console_data(message: str = 'Введите значение: ', user_type: type = int):
    """Функция ввода данных с консоли

    Args:
        message (str): сообщение, которое будет показано пользователю
        user_type (type): тип данных, которые пользователь требует

    Returns:
        _type_: полученное значение
    """
    while True:
        user_data = input(message)
        try:
            user_data = user_type(user_data)
        except Exception as ex:
            print(ex)
        else:
            return user_data

def get_start_data():  
    """Функция для настройки базовых параметров (границы, попытки)

    Returns:
        (int,int,int): Левая граница, правая граница, количество попыток
    """
    while True:
        left_edge = get_console_data('Введите левую границу: ')
        right_edge = get_console_data('Введите правую границу: ')
        tries = get_console_data('Введите количество попыток: ')
        try:
            assert right_edge > left_edge, 'Значения границ неверны!'
            assert tries < right_edge-left_edge, 'Попыток слишком много!'
        except AssertionError as ex:
            print(ex)
        else:
            return left_edge, right_edge, tries

def user_try():
    for i in range(tries):
        while True:
            user_number = get_console_data('Введите число: ')

            try:
                assert not (user_number < left_edge or
                            user_number > right_edge), f'Ошибка, число должно быть в диапазоне от [{left_edge},{right_edge}]'
            except AssertionError as ex:
                print(ex)
            else:
                break
        if user_number == random_number:
            print('Угадал!!')
            break
        else:
            print('Не угадал')
    else:
        print('Попытки закончились. Игра окончена')



left_edge, right_edge, tries = get_start_data()
random_number = random.randint(left_edge, right_edge)
user_try()

