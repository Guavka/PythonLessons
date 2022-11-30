# dict - коллекции, у которых есть структура

users_list = [
    ['User1', 123],  # 0
    ['User2', 125],  # 1
    ['User3', 124],  # 2
]
print(users_list[2][0])  # User3

user_dict = {
    'User1': {
        'login': 'User1',
        'password': 123
    },
    'User2': {
        'login': 'User2',
        'password': 125
    },
    'User3': {
        'login': 'User3',
        'password': 124
    },
}
print(user_dict['User3']['login'])  # User3


phone_book_list = [
    [
        'Contact1',
        [
            [
                'Work',
                12345
            ]
        ]
    ],
    ['Contact2', [['Work', 12345], ['Work2', 12345]]],
    ['Contact3', [['Work', 12345], ['Work2', 12345], ['Work3', 866]]],
]

print(phone_book_list[2][1][2][1])  # 866

phone_book_dict = {
    'Contact1': {
        'name': 'Contact1',
        'numbers': {
            'Work': 12345
        }},
    'Contact2': {
        'name': 'Contact2',
        'numbers': {
            'Work': 12345,
            'Work2': 12345
        }},
    'Contact3': {
        'name': 'Contact2',
        'numbers': {
            'Work': 12345,
            'Work2': 12345,
            'Work3': 866
        }},
}

print(phone_book_dict['Contact3']['numbers']['Work3'])  # 866

username_list = [['User1', 15], ['User2', 18]]
username_dict = {
    'User1': 15,
    'User2': 18
}

# Вывести на экран всех, кто старше 18
for user in username_list:
    if user[1] >= 18:
        print(user[0])

for user in username_dict:
    if username_dict[user] >= 18:
        print(user)

# Добавить пользователя в базу
# list
login = 'User2'
age = 14
for user in username_list:
    if user[0] == login:
        print('Логин занят')
        break
else:
    username_list.append([login, age])
    print('Добавил!')
print(username_list)

# dict
if login in username_dict:
    print('Логин занят')
else:
    username_dict[login] = age
print(username_dict)

# set - множество, специфическая коллекция
print('------set')
number_set1 = {1, 2, 3, 4}
number_set2 = {4, 5, 6, 7}

print(number_set1.difference(number_set2))  # {1, 2, 3}

print(number_set1.intersection(number_set2))  # {4 }

print(number_set1.union(number_set2))  # {1, 2, 3, 4, 5, 6, 7}


friend_set = {'Андрей', 'Миша', 'Альбина'}
friend_set2 = {'Алексей', 'Маша', 'Альбина'}

print(friend_set.intersection(friend_set2))  # Альбина
