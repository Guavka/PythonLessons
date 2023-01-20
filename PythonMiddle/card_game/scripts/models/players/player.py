from typing import List

from scripts.models.card import Card


class Player:
    # Поля
    __hand: List[Card] = []
    __score = 0

    __name: str
    __money: int

    # Поля

    # Свойства
    @property
    def name(self):
        return self.__name

    @property
    def money(self):
        return self.__money

    @property
    def score(self):
        return self.__score

    @property
    def hand(self):
        from copy import deepcopy
        return deepcopy(self.__hand)

    # Свойства

    # Проверки данных

    def __check_name(self, name: str):
        assert type(name) == str, 'Имя должно быть строкой'
        assert name != '', 'Имя не должно быть пустым'

        self.__name = name

    def __check_money(self, money: int):
        assert int(money) > 0, 'Денег должно быть больше 0'

        self.__money = money

    # Проверки данных


    # Публичные функции
    def clear_hand(self):
        self.__hand = []
        self.__score = 0

    def add_card(self, card: Card):
        assert isinstance(card, Card), 'Карта не карта'

        self.__hand.append(card)
        self.__score += card.value

    def add_money(self, money: int):
        assert int(money) > 0, 'Денег должно быть больше 0'

        self.__money += money

    def subtract_money(self, money: int):
        assert int(money) > 0, 'Денег должно быть больше 0'

        self.__money -= money
    # Публичные функции
    
    def __init__(self, name='John', money=1000) -> None:
        self.__check_name(name)
        self.__check_money(money)
