from typing import Literal

Names = Literal[2, 3, 4, 5, 6, 7, 8, 9,
                10, 'Валет', 'Дама', 'Король', 'Туз']
Suits = Literal['черви', 'пики', 'крести', 'бубны']


class Card:
    __possible_names__: Names = [2, 3, 4, 5, 6, 7, 8, 9,
                                 10, 'Валет', 'Дама', 'Король', 'Туз']

    __posible_suits__: Suits = ['черви', 'пики', 'крести', 'бубны']

    __posible_values__ = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    __name: Names
    __suit: Suits

    __value: int

    @property
    def name(self):
        return self.__name

    @property
    def suit(self):
        return self.__suit

    @property
    def value(self):
        return self.__value

    def __check_name(self, name: Names):
        assert name in self.__possible_names__, 'Неподходящее имя'
        self.__name = name

    def __check_suit(self, suit: Suits):
        assert suit in self.__posible_suits__, 'Неподходящая масть'
        self.__suit = suit

    def __init__(self, name: Names, suit: Suits) -> None:
        self.__check_name(name)
        self.__check_suit(suit)

        if name in self.__posible_values__:
            self.__value = name
        elif name in ['Валет', 'Дама', 'Король']:            
            self.__value = 10
        else:
            self.__value = 11
            
    def __str__(self) -> str:
        return f'{self.name} {self.suit}'
         