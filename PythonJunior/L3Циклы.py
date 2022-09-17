# Циклы - потоврения определенного сегмента кода N раз

'''
range - коллекция целых чисел от левая_граница до правая_граница
'''

temp = range(10)  # список целых чисел от 0 до 9
temp = range(5, 15)  # список целых чисел от 5 до 14
temp = range(3, 8, 2)  # список целых чисел от 5 до 14, через 1

'''
for - итерационный цикл - работает N раз или меньше

for имя_переменной in коллекция:
    действия
'''
for number in temp:
    print(number)

'''
for ... else - цикл поиска

for имя_переменной in коллекция:
    if условие:
        break
else:
    действие_если_не_нашли
'''

temp = range(0, 1000, 3)
for number in temp:
    if number == 665:
        print('Я нашел!!!')
        break
else:
    print('Я не нашел(')


# Операторы циклов:
#   break - выйти из цикла
#   continue - перейти к следующему шагу

number = 5
for number_iter in range(number, number*2):
    if number_iter > 6:
        break
    print(number_iter)

print('-----------')

left_edge = 5
for number in range(left_edge, left_edge*2):
    if number % 2 == 0:
        continue
    print(number)

print('-------------While----------')
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


# Ввод возраста

for try_number in range(3):
    user_age = input('Введи возраст for: ')
    user_age = int(user_age)
    if user_age < 0 or user_age > 120:
        print('Ошибка! Возраст должен быть в диапазоне [0,120]')
    else:
        break
else:
    print('Попытки закончились')
    
while True:
    user_age = input('Введи возраст while: ')
    user_age = int(user_age)
    if user_age < 0 or user_age > 120:
        print('Ошибка! Возраст должен быть в диапазоне [0,120]')
    else:
        break
    
    
# Слоты (рулетка)
import random

money = 1000
count = 1
while True:
    money -= 100
    rand_number = random.randint(0,1)
    if rand_number == 1:
       money += 100*2
       print('Выигрыш')
    else:
       print('Проигрыш')
    print(f'{count}.Ваши деньги :{money}')
    count += 1
    
    if money <= 0:
        print('Игра окончена')
        break
    