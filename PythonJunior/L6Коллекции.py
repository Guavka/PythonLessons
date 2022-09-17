# списки - коллекции, в которых данные находятся неупорядоченно, согласно некой логике

import copy
temp = ['Alex', 18, True]  # нет смысла просто мусорник из данных

users_list = ['Alex', 'Guavka', 'Den']  # логичный список

# получение значения
result = users_list[0]  # Alex
print(result)
result = users_list[1]  # Guavka
print(result)
result = users_list[2]  # Den
print(result)

# присвоение значения
users_list[0] = 'test'

print(users_list)

# итерации по списку

for user in users_list:
    print(f'Username: {user}')


# сложные списки
users_list = [
    ['Guavka', 14],
    ['Den', 50],
    ['Alex', 18]
]
print(users_list[0][0])  # Guavka
print(users_list[1][1])  # 27
print(users_list[2][0])  # Alex


# копирование списков
print('---------- копирование списков')
number1 = 5
number2 = number1
number2 += 1
print(f'Number1: {number1}\nNumber2: {number2}')  # 5 6

user_list = ['user1', 'user2']
user_list2 = user_list
user_list2[0] = 'Alex'
print(user_list, user_list2)

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
print('----------shallow copy')
# shallow copy - поверхностное копирование
user_list = ['user1', 'user2']  # Ref->[val,val]
user_list2 = user_list.copy()
user_list2[0] = 'Alex'
print(user_list, user_list2)

print('----------deep copy')
# deep copy - глубокое копирование
# Ref -> [ Ref->[val,val], Ref->[val,val]]
user_list = [['user1', 12], ['user2', 15]]
user_list2 = user_list.copy()
user_list2[0][0] = 'Alex'
print(user_list, user_list2)  # не работает

user_list = [['user1', 12], ['user2', 15]]

user_list2 = []
for user in user_list:
    user_list2.append(user.copy())

user_list2[0][0] = 'Alex'
print(user_list, user_list2)

print('----------import copy')
user_list = [['user1', 12], ['user2', 15]]
user_list2 = copy.deepcopy(user_list)
user_list2[0][0] = 'Alex'
print(user_list, user_list2)

# словари - коллекция формата "ключ-значение", используется для храниения структурированной информации
print('-----------DICTS')
users_age_dict = {
    'Guavka': 28,
    'Den': 27
}

print(users_age_dict)

# получение значения
result = users_age_dict['Guavka']  # 28
print(result)
result = users_age_dict['Den']  # 27
print(result)

# присвоение значения
users_age_dict['Guavka'] = 30
print(users_age_dict)

# итерации по списку
for user in users_age_dict:  # итерации по ключу
    print(f'Username: {user}')

for age in users_age_dict.values():  # итерации по значению
    print(f'Age: {age}')

# ---- Simple example - вывести только тех, кому больше 18
print('-----------Example')

user_list = [['user1', 12], ['user2', 19]]
for user in user_list:
    if user[1] >= 18:
        print(f'Username: {user[0]}\nAge: {user[1]}\n-----------')

users_age_dict = {
    'user1': 12,
    'user2': 19
}
for user in users_age_dict:
    age = users_age_dict[user]
    if age >= 18:
        print(f'Username: {user}\nAge: {age}\n-----------')

# ----


phone_book_list = [
    [
        'Alex',
        [
            ['Home', 1231231232],
            ['Work', 1651321321]
        ]
    ],
    [
        'Den',
        [
            ['Home', 1231231232],
        ]
    ],
    [
        'Daria',
        [
            ['Home', 1231231232],
            ['Home2', 555385],  # !
            ['Home3', 1231231232],
        ]
    ],
]

print(phone_book_list[2][1][1][1])  # 555385


phone_book_dict = {
    'Alex': {
        'Home': 1231231232,
        'Work': 1651321321
    },
    'Den': {
        'Home': 1231231232
    },
    'Daria': {
        'Home': 1231231232,
        'Home2': 555385,
        'Home3': 1231231232,
    },
}

print(phone_book_dict['Daria']['Home2'])  # 555385

# tuple - кортеж - список, но его нельзя менять
print('---------- tuple')

user_tuple = ('user1', 'user2')
print(user_tuple[0])
# user_tuple[0] = 'test' вызывает ошибку


users_tuple = (
    ('Guavka', 28),
    ('Den', 27),
)
print(users_tuple)

users_tuple2 = (
    ['Guavka', 28],
    ['Den', 27],
)
print(users_tuple2)
users_tuple2[1][0] = 'Hackerman'
print(users_tuple2)


def init_numbers():
    return 5, 10, 15


left, mid, right = init_numbers()


# set - множества - коллекция, состоящая из уникальных значений
print('-------set')
user_set = {'user1', 'user2', 'user1'}
print(user_set)


number_set1 = {1, 2, 3, 4}
number_set2 = {4, 5, 6, 7}

print(number_set1.difference(number_set2))  # {1, 2, 3}
print(number_set1.intersection(number_set2))  # {4}
print(number_set1.union(number_set2))  # {1, 2, 3, 4, 5, 6, 7}
