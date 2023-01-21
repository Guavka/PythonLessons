# Условия
number1 = 5
number2 = 2

'''
Операторы условия - знаки, которые можно исмпользовать при сравнении
>  - больше - первое значение больше второго (5>2) - правда, (5>5) - ложь
<  - меньше - первое значение меньше второго (2<5) - правда, (2<2) - ложь
>= - больше-равно - первое значение больше или равно второму (5>=2)-правда, (5>=5)-правда
<= - меньше-равно - первое значение меньше или равно второму (2<=5)-правда, (2<=2)-правда
== - равенство - первое значение равно второму (5==5),(2==2)
!= - не равно - первое значение не равно второму (5!=2)
'''

'''
Укороченный if
if условие:
    дейcтвия_если_условие_выполняется
'''
if number1 > number2:
    print('number1 > number2')
    print('number1 > number2')
print('Привет!')

'''
Обычный if
if условие:
    дейcтвия_если_условие_выполняется
else:
    дейcтвия_если_условие_не_выполняется
'''
if number1 > number2:
    print('number1 > number2')
else:
    print('number1 <= number2')

'''
Каскадный if (версия 1)
if условие:
    дейcтвия_если_условие_выполняется
else:
    if условие2:
        дейcтвия_если_условие2_выполняется
    else:
        дейcтвия_если_условие2_не_выполняется
'''

mark = 1
if mark == 5:
    print('Отличник')
else:
    if mark == 4:
        print('Хорошист')
    else:
        if mark == 3:
            print('Троечник')
        else:
            if mark == 2:
                print('Двоечник')
            else:
                print('Это кол!')

'''
Каскадный if (версия 2) - лучше использовать ее
if условие:
    дейcтвия_если_условие_выполняется
elif условие2:
    дейcтвия_если_условие_выполняется
else:
    дейcтвия_если_условие_не_выполняется
'''

mark = 1
if mark == 5:
    print('Отличник')
elif mark == 4:
    print('Хорошист')
elif mark == 3:
    print('Троечник')
elif mark == 2:
    print('Двоечник')
else:
    print('Это кол!')

if number1 > number2:
    print('number1 > number2')
elif number1 < number2:
    print('number1 < number2')
else:
    print('number1 = number2')

'''
Результат условия в переменной
переменная = условие
'''

is_great = number1 > number2  # True


'''
Инлайновый if
переменная = значение_если_условие_выполняется if условие else значение_если_условие_не_выполняется
'''

if number1 > number2:
    print('number1 > number2')
else:
    print('number1 <= number2')

result = 'number1 > number2' if number1 > number2 else 'number1 <= number2'
print(result)


if number1 > number2:
    print('number1 > number2')
elif number1 < number2:
    print('number1 < number2')
else:
    print('number1 = number2')
result = 'number1 > number2' if number1 > number2 else 'number1 < number2' if number1 < number2 else 'number1 = number2'


'''
Сложные условия - условия, где больше 1 условия
Для написания сложных условий, используются операторы: 
and - логическое И - И ТО И ТО выполняется (5 > 1 and 5 > 3) - True
or - логическое ИЛИ - первое ИЛИ второе выполняется (5 > 0 or 5 > 8) - True
not - отрицание правда становится ложью и наоборот (not (5 > 8)) - True 
'''

помыл_посуду = False
сделал_уроки = True

if помыл_посуду:
    if сделал_уроки:
        print('Иди гуляй')
    else:
        print('Ты не сделал все домашние дела')
else:
    print('Ты не сделал все домашние дела')

if помыл_посуду and сделал_уроки:
    print('Иди гуляй')
else:
    print('Ты не сделал все домашние дела')


помыл_полы = True
if помыл_посуду or помыл_полы:
    print('Иди гуляй')
else:
    print('Ты не сделал все домашние дела')

# Сложное условие - громоздко, лучше не использовать
if сделал_уроки and (помыл_посуду or помыл_полы):
    print('Иди гуляй')
else:
    print('Ты не сделал все домашние дела')

# Выносим условие в отдельную переменную - удобно, рекомендую!!!!
могу_гулять = сделал_уроки and (помыл_посуду or помыл_полы)
if могу_гулять:
    print('Иди гуляй')
else:
    print('Ты не сделал все домашние дела')


могу_гулять = сделал_уроки and (помыл_посуду or помыл_полы)
if могу_гулять:
    сообщение = 'Иди гуляй'
else:
    сообщение = 'Ты не сделал все домашние дела'
print(сообщение)

# Делаем условие инлайновым(ТОЛЬКО ДЛЯ ПРОСТЫХ ДЕЙСТВИЙ)

'''
Было
if сделал_уроки and (помыл_посуду or помыл_полы):
    print('Иди гуляй')
else:
    print('Ты не сделал все домашние дела')
'''

могу_гулять = сделал_уроки and (помыл_посуду or помыл_полы)
сообщение = 'Иди гуляй' if могу_гулять else 'Ты не сделал все домашние дела'
print(сообщение)

# Простое приложение для закрепления условий
# Задача - ввести число от 1 до 120 и определить ребенок, подросток, взрослый или пожилой человек

''' 
age = 50
if age < 14:
    print('Ребенок')
elif age < 21:
    print('Подросток')
elif age < 60:
    print('Взрослый')
else:
    print('Пожилой')
'''

''' 
age = 500
if 0 < age <= 120: # возраст > 0 and возраст <= 120
    if age < 14:
        print('Ребенок')
    elif age < 21:
        print('Подросток')
    elif age < 60:
        print('Взрослый')
    else:
        print('Пожилой')
else:
    print('Введите число от 1 до 120')
'''

''' 
age = 500
if not (0 < age <= 120): # age <= 0 or age > 120
    print('Введите число от 1 до 120')    
else:
    if age < 14:
        print('Ребенок')
    elif age < 21:
        print('Подросток')
    elif age < 60:
        print('Взрослый')
    else:
        print('Пожилой')
'''

'''
age = 500
if not (0 < age <= 120):
    message = 'Введите число от 1 до 120'
else:
    if age < 14:
        message = 'Ребенок'
    elif age < 21:
        message = 'Подросток'
    elif age < 60:
        message = 'Взрослый'
    else:
        message = 'Пожилой'

    #message =  'Ребенок' if age < 14 else 'Подросток' if age < 21 else 'Взрослый' if age < 60 else 'Пожилой'

print(message)
'''

'''
min_age = 1
max_age = 150

name_child = 'Ребенок'
edge_child = 16

name_teen = 'Подросток'
edge_teen = 25

name_adult = 'Взрослый'
edge_adult = 75

name_old = 'Пожилой'

err_message = 'Введите число в диапазоне'

age = 600

if not (min_age <= age <= max_age):
    # Введите число от 1 до 120
    message = f'{err_message} [{min_age}, {max_age}]'
else:
    if age < edge_child:
        message = name_child
    elif age < edge_teen:
        message = name_teen
    elif age < edge_adult:
        message = name_adult
    else:
        message = name_old
print(message)
'''

min_age = 1
max_age = 150

name_child = 'Ребенок'
edge_child = 16

name_teen = 'Подросток'
edge_teen = 25

name_adult = 'Взрослый'
edge_adult = 75

name_old = 'Пожилой'

err_message = 'Введите число в диапазоне'

age = input(f'{err_message} [{min_age}, {max_age}]: ') # 5 -> '5' 
age = int(age) # int('5') -> 5

if not (min_age <= age <= max_age):
    # Введите число от 1 до 120
    message = f'{err_message} [{min_age}, {max_age}]'
else:
    if age < edge_child:
        message = name_child
    elif age < edge_teen:
        message = name_teen
    elif age < edge_adult:
        message = name_adult
    else:
        message = name_old
print(message)
