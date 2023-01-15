
# Циклы - повторение определенного сегмента кода N раз

print('__________Базовая информация')
number1 = 5

number1 += 1
number1 += 1
number1 += 1
number1 += 1
number1 += 1
number1 += 1
number1 += 1
number1 += 1

print(number1)

number1 = 5
for step in range(100):
    number1 += 1
print(number1)

'''
range - коллекция целых чисел от левая_граница до правая_граница
range(левая_граница,правая_граница, шаг)
'''

temp = range(10)  # список целых чисел от 0 до 9
# [0,1,2,3,4,5,6,7,8,9]

temp = range(5, 15)  # список целых чисел от 5 до 14
# [5,6,7,8,9,10,11,12,13,14]

temp = range(3, 8, 2)  # список целых чисел от 3 до 7, через 1
# [3,5,7]

print('__________Цикл for')

'''
for - итерационный цикл - работает N раз или меньше
for имя_переменной in коллекция:
    действия
'''
for number in range(1, 13):
    print(number)

print('__________Цикл for ... else')

'''
for ... else - цикл поиска
for имя_переменной in коллекция:
    if условие:
        break
else:
    действие_если_не_нашли
'''

# Поиск числа без for ... else
found_number = 665
is_found = False
for number in range(1000):
    if number == found_number:
        is_found = True
        break

message = 'Я нашел!!!' if is_found else 'Я не нашел('
print(message)

# Поиск числа с for ... else
found_number = 665
for number in range(1000):
    if number == found_number:
        message = 'Я нашел!!!'
        break
else:
    message = 'Я не нашел('
print(message)

print('__________Операторы циклов')
print('__________Оператор break')
# Операторы циклов:
#   break - выйти из цикла
#   continue - перейти к следующему шагу

number = 5
for iter in range(number, number * 2):
    if iter > 6:
        break
    print(iter)

print('__________Оператор continue')
number = 5
for iter in range(number, number * 2):
    if iter == 6:
        continue
    print(iter)


print('__________Цикл while')
'''
while - цикл работаект ПОКА выполняется условие
while условие:
    действия
'''

number1 = 5
number2 = 20
while number1 < number2:
    number1 += 1
    print(number1)
    
number1 = 5
number2 = 20  
for i in range(number2 - number1):
    number1 += 1
    print(number1)

# import random

from random import randint

while randint(1, 3) != 2:
    print('Не равен')


# Ввод возраста
print('__________Ввод возраста')
for tries in range(3):
    # ввод возраста с консоли (терминала)
    age = input('Введи возраст for: ')
    # пробуем превратить строку в число(приведение типов)
    age = int(age)
    if age < 0 or age > 120:
        print('Ошибка! Возраст должен быть в диапазоне [0,120]')
    else:
        break
else:
    print('Попытки закончились')


while True:
    age = input('Введи возраст while: ')
    age = int(age)
    if age < 0 or age > 120:
        print('Ошибка! Возраст должен быть в диапазоне [0,120]')
    else:
        break

# Слоты (рулетка)
print('__________Слоты (рулетка)')

score = 1000
round_number = 1
while True:
    score -= 100
    com_number = randint(0, 1)
    if com_number == 1:
        score += 100*2
        message = 'Вы выиграли'
    else:
        message = 'Вы проиграли'
    print(f'{message}\n{round_number}.Ваши очки: {score}')
    
    #print(message + '\n' + str(round_number)+'.Ваши очки: ' + str(score))
    round_number += 1

    if score <= 0:
        print('Игра окончена')
        break


# Слоты (рулетка) с контролем игрока
print('__________Слоты (рулетка) с контролем игрока')

score = 1000
round_number = 1

min_bet = 10
max_bet = 500

while True:
    bet = input(
        f'Введите ставку от {min_bet} до {max_bet}: ')  # '50'
    bet = int(bet)  # пробуем превратить строку в число(приведение типов)
    if bet > score:
        print(f'Ошибка вы можете поставить максимум {score} очков')
    else:
        if min_bet <= bet <= max_bet:
            score -= bet
            com_number = randint(0, 1)
            if com_number == 1:
                score += bet*2
                print('Выигрыш')
            else:
                print('Проигрыш')
            print(f'{round_number}.Ваши очки: {score}')
            round_number += 1

            if score <= 0:
                print('Игра окончена')
                break
        else:
            print(f'Ставка должна быть от  {min_bet} до {max_bet}')


# Слоты (рулетка) с контролем игрока после чистки
print('__________Слоты (рулетка) с контролем игрока после чистки')

score = 1000
round_number = 1

min_bet = 10
max_bet = 500

# Бесконечный цикл для игры
while True:
    # Бесконечный цикл для выбора ставки
    while True:
        bet = input(
            f'Введите ставку от {min_bet} до {max_bet}: ')  # '50'
        # пробуем превратить строку в число(приведение типов)
        bet = int(bet)
        if bet > score:
            print(f'Ошибка вы можете поставить максимум {score} очков')
        else:
            if min_bet <= bet <= max_bet:
                break
            else:
                print(f'Ставка должна быть от  {min_bet} до {max_bet}')

    score -= bet
    com_number = randint(0, 1)
    if com_number == 1:
        score += bet*2
        print('Выигрыш')
    else:
        print('Проигрыш')
    print(f'{round_number}.Ваши очки: {score}')
    round_number += 1

    if score <= 0:
        print('Игра окончена')
        break
