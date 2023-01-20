'''
Алгоритм игры Black Jack
1. Генерируем колоду (перемешиваем ее)
2. Создаем игрока и банк
3. Раздаем по 2 карты
4. Цикл пока оба не скажут "пасс"
5. Подведение итогов
'''

'''
from random import shuffle

deck = []

# 4 масти, карт 52/4 = 13 итераций

for number in range(2, 14):
    name = number
    value = number

    if number > 10:
        value = 10
        if number == 11:
            name = 'Валет'
        elif number == 12:
            name = 'Дама'
        elif number == 13:
            name = 'Король'
        else:
            value = 11
            name = 'Туз'

    deck.append({'name': name,
                 'value': value,
                 'suit': 'черви',
                 })
    deck.append({'name': name,
                 'value': value,
                 'suit': 'крести',
                 'name': name})
    deck.append({'name': name,
                 'value': value,
                 'suit': 'пики'
                 })
    deck.append({'name': name,
                 'value': value,
                 'suit': 'бубны'})

shuffle(deck)

player = {
    'hand': [],
    'score': 0
}

bank = {
    'hand': [],
    'score': 0
}


player['hand'].append(deck.pop())
player['hand'].append(deck.pop())

bank['hand'].append(deck.pop())
bank['hand'].append(deck.pop())


while True:
    score = 0
    for card in player['hand']:
        score += card['value']
        print(card['name'], card['suit'])

    print(f'Your score: {score}\nGet card?\n1 - Yes\n2 - No')
    user_choose = input()
    if user_choose == '1':
        player['hand'].append(deck.pop())
    elif user_choose == '2':
        break
    else:
        print('Error! Input 1 or 2')


while True:
    score = 0
    for card in bank['hand']:
        score += card['value']

    if score >= 15:
        break
    else:
        bank['hand'].append(deck.pop())


user_score = 0
for card in player['hand']:
    user_score += card['value']

bank_score = 0
for card in bank['hand']:
    bank_score += card['value']

print(f'player: {player["hand"]}')
print(f'bank: {bank["hand"]}')

print(f'Player score: {user_score}\nBank score: {bank_score}')

if bank_score == user_score:
    print('Draw')
elif bank_score > 21:
    if user_score < bank_score:
        print('Player win')
    else:
        print('Bank win')
else:
    if user_score < bank_score:
        print('Bank win')
    else:
        print('Player win')
'''

'''
Алгоритм игры Black Jack
1. Генерируем колоду (перемешиваем ее)
2. Создаем игрока и банк
3. Раздаем по 2 карты
4. Цикл пока оба не скажут "пасс"
5. Подведение итогов
'''

from typing import Dict, List
def init_deck(start_value=2) -> List[Dict[str, str|int]]:
    """Функция, которая генерирует колоду карт

    Returns:
        List[Dict[str, str|int]]: колода карт
    """
    from random import shuffle
    deck = []

    # 4 масти, карт 52/4 = 13 итераций

    for number in range(start_value, 14):
        name = number
        value = number

        if number > 10:
            value = 10
            if number == 11:
                name = 'Валет'
            elif number == 12:
                name = 'Дама'
            elif number == 13:
                name = 'Король'
            else:
                value = 11
                name = 'Туз'

        deck.append({'name': name,
                    'value': value,
                     'suit': 'черви',
                     })
        deck.append({'name': name,
                    'value': value,
                     'suit': 'крести',
                     'name': name})
        deck.append({'name': name,
                    'value': value,
                     'suit': 'пики'
                     })
        deck.append({'name': name,
                    'value': value,
                     'suit': 'бубны'})

    shuffle(deck)
    return deck


def init_players(deck: List[Dict[str, str | int]], start_card=2):
    player = {
        'hand': [],
        'score': 0
    }

    bank = {
        'hand': [],
        'score': 0
    }

    for i in range(start_card):
        player['hand'].append(deck.pop())
        bank['hand'].append(deck.pop())

    return player, bank


def bank_get(deck: List[Dict[str, str | int]], bank_player: Dict[str, str]):
    while True:
        score = 0
        for card in bank_player['hand']:
            score += card['value']

        if score >= 15:
            break
        else:
            bank_player['hand'].append(deck.pop())


def player_get(deck: List[Dict[str, str | int]], user_player: Dict[str, str]):
    while True:
        score = 0
        for card in user_player['hand']:
            score += card['value']
            print(card['name'], card['suit'])

        user_choose = input(f'Your score: {score}\nGet card?\n1 - Yes\n2 - No')
        if user_choose == '1':
            user_player['hand'].append(deck.pop())
        elif user_choose == '2':
            break
        else:
            print('Error! Input 1 or 2')


def get_winner(user_player: Dict[str, str], bank_player: Dict[str, str]):
    user_score = 0
    for card in user_player['hand']:
        user_score += card['value']

    bank_score = 0
    for card in bank_player['hand']:
        bank_score += card['value']

    print(f'player: {user_player["hand"]}')
    print(f'bank: {bank_player["hand"]}')

    print(f'Player score: {user_score}\nBank score: {bank_score}')

    if bank_score == user_score:
        print('Draw')
    elif bank_score > 21:
        if user_score < bank_score:
            print('Player win')
        else:
            print('Bank win')
    else:
        if user_score < bank_score:
            print('Bank win')
        else:
            print('Player win')


deck = init_deck()
player, bank = init_players(deck)

bank_get(deck, bank)
player_get(deck, player)

get_winner(player, bank)
