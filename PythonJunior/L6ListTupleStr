# списки - коллекции, в которых данные находятся неупорядоченно, согласно некой логике

temp = ['Alex', 18, True]  # нет смысла, просто мусорник из данных

users_list = ['Alex', 'Guavka', 'Den']  # логичный список

# получение значения
result = users_list[0]  # Alex
print(result)
result = users_list[1]  # Guavka
print(result)
result = users_list[2]  # Den
print(result)

# присвоение значения
users_list[0] = 'test'  # ['test', 'Guavka', 'Den']

print(users_list)


users_list = ['Alex', 'Guavka', 'Den']
# итерации по списку

for i in range(2, 5):
    print(i)

print('-------------print by iterator')
for user in users_list:
    print(f'Username: {user}')

print('-------------print by index')
for i in range(len(users_list)):
    print(f'Username: {users_list[i]}')

drinks = ['Кофе', 'Капучино', 'Чай']

print('-------------print by iterator')
index = 1
for drink in drinks:
    print(f'{index}.{drink}')
    index += 1

print('-------------print by index')
for i in range(len(drinks)):
    print(f'{i + 1}.{drinks[i]}')

print('-------------Встроенные функции')
# Встроенные функции
drinks = ['Кофе', 'Капучино', 'Чай']

drinks.append('Молоко')  # добавляем элемент в конец списка
print(drinks)

drinks.insert(1, 'Какао')  # добавляет элемент по нужному индексу
print(drinks)

drinks.insert(1, 'Молоко')  # добавляет элемент по нужному индексу
print(drinks)

milk_index = drinks.index('Молоко')  # возвращает индекс молока
print(milk_index)

drinks.remove('Капучино')  # удаляет элемент из списка
print(drinks)

drinks.pop()  # удаляет последний элемент
print(drinks)

drinks.copy()  # поверхностное копирование


# Value type, Reference type
'''
простые типы - Value type - Значащий тип
int
str 
bool
float
'''

'''
сложные типы - Reference type - Ссылочные типы
list
tuple
dict
set
все кастомные классы
'''

# Копировние данных

print('---------------Копирование данных')
drinks = ['Кофе', 'Капучино', 'Чай']
drinks2 = drinks

print(f'drinks = {drinks}')
print(f'drinks2 = {drinks2}')

drinks2[1] = 'Лимонад'

print(f'drinks = {drinks}')
print(f'drinks2 = {drinks2}')

print('-----------------Shallow copy')
# Shallow copy

drinks = ['Кофе', 'Капучино', 'Чай']
drinks2 = drinks.copy()

print(f'drinks = {drinks}')
print(f'drinks2 = {drinks2}')

drinks2[1] = 'Лимонад'

print(f'drinks = {drinks}')
print(f'drinks2 = {drinks2}')

print('----------------Вложенные списки')
# Вложенные списки

users_list = [
    ['Alex', 28, True],
    ['Daria', 18, True],
    ['Den', 27, True]
]

# Получение доступа

print(users_list[0][0])  # Alex
print(users_list[1][2])  # True
print(users_list[2][1])  # 27

phone_book = [
    [
        'Alex',
        28,
        [
            ['Домашний', 12342131],
            ['Мобильный', 1654871],
        ]
    ],
    [
        'Daria',
        18,
        [
            ['Домашний', 12342131],
            ['Мобильный', 1654871],
            ['Мобильный2', 132463216521],
        ]
    ],
]

print(phone_book[1][2][2][0])  # Мобильный2

phone_book.append([
    'Den',
    27,
    [
        ['Домашний', 12342131],
    ]
])

# Deep copy - глубокое копирование
print('--------------------Deep copy')

users_list = [
    ['Alex', 28],
    ['Daria', 18]
]

users_list2 = users_list.copy()

print(f'list1 = {users_list}')
print(f'list2 = {users_list2}')

# Копируется только первый слой
users_list2[1] = ['Den', 27]
print(f'list1 = {users_list}')
print(f'list2 = {users_list2}')

users_list2[0][0] = 'Test'
print(f'list1 = {users_list}')
print(f'list2 = {users_list2}')

# Ручное deep copy
print('------------Ручное deep copy')
users_list = [
    ['Alex', 28],
    ['Daria', 18]
]
users_list2 = []

for user in users_list:
    temp = user.copy()
    users_list2.append(temp)

print(f'list1 = {users_list}')
print(f'list2 = {users_list2}')
users_list2[0][0] = 'Test'
print(f'list1 = {users_list}')
print(f'list2 = {users_list2}')

# Модуль copy
print('------------------Модуль copy')
phone_book = [
    [
        'Alex',
        28,
        [
            ['Домашний', 12342131],
            ['Мобильный', 1654871],
        ]
    ],
    [
        'Daria',
        18,
        [
            ['Домашний', 12342131],
            ['Мобильный', 1654871],
            ['Мобильный2', 132463216521],
        ]
    ],
]

from copy import deepcopy
phone_book2 = deepcopy(phone_book)

print(f'phone_book = {phone_book}')
print(f'phone_book2 = {phone_book2}')

phone_book2[0][2][0][0] = 'Дом'

print(f'phone_book = {phone_book}')
print(f'phone_book2 = {phone_book2}')

# Срезы - особый механизм, позволяющий получать копию коллекции или ее участка
print('-----------------Срезы')
numbers = [1, 2, 5, 7, 9, 0]
numbers2 = numbers.copy()
numbers2.remove(numbers[0])
print(numbers)
print(numbers2)

numbers = [1, 2, 5, 7, 9, 0]
numbers2 = numbers[0:len(numbers)-1:1]
numbers2 = numbers[::]  # [1, 2, 5, 7, 9, 0]
print(numbers2)
numbers2 = numbers[1::]  # [2, 5, 7, 9, 0]
print(numbers2)
numbers2 = numbers[:4:]  # [1, 2, 5, 7]
print(numbers2)
numbers2 = numbers[::2]  # [1, 5, 9]
print(numbers2)


# Tuple - кортежи - списки, у которых нельзя поменять данные

print('-------------Tuple')
users_list = ['Alex', 'Den']
print(users_list)
users_list[1] = 'Daria'
print(users_list)

user_tuple = (
    ('Alex', 28),
    ('Daria', 18)
)
print(user_tuple)
#user_tuple[1][0] = 'Den'
# print(user_tuple)

# Строки - частный случай кортежей
print('---------------Строки')
string = 'Hello'
string_list = ['H', 'e', 'l', 'l', 'o']

for s in string:
    print(s)

drinks = ['кофе', 'чАй', 'ЛиМоНаД']
for drink in drinks:
    print(drink.lower().capitalize())

word = 'Hello'
word = word.replace('l', 'X')
print(word)

word = 'Hello'
print(word[:len(word)-1:])

# Кофемашина
print('-------------------Кофемашина ')
drink_list = [
    [
        'Кофе',
        [
            ['200мл', 150],
            ['300мл', 200],
            ['350мл', 250],
        ]
    ],
    [
        'Чай',
        [
            ['300мл', 100],
            ['350мл', 150],
        ]
    ],
]

print('Добро пожаловать, выберите напиток!')
index = 1
for drink in drink_list:
    print(f'{index}.{drink[0]}')
    index += 1
print(f'{index}.Выход')

while True:
    user_choose = input()
    try:
        user_choose = int(user_choose)
        if user_choose == len(drink_list) + 1:
            print('Вы нажали выход!')
            break
        else:
            assert user_choose in range(1, len(drink_list)+1), ''
            drink = drink_list[user_choose-1]
            break
    except AssertionError:
        print(f'Введите число от 1 до {len(drink_list) + 1}')
    except Exception:
        print('Ввведите число цифрами!')
print(drink)
