from scripts.models.card import Card


class Deck:
    from typing import List

    __deck: List[Card] = []
    __start_value: int

    def get_card(self):
        try:
            return self.__deck.pop()
        except:
            self.__init__(self.__start_value)
            return self.__deck.pop()

    def __init__(self, start_value=2) -> None:
        from random import shuffle

        self.__start_value = start_value

        for number in range(start_value, 14):
            name = number

            if number > 10:
                if number == 11:
                    name = 'Валет'
                elif number == 12:
                    name = 'Дама'
                elif number == 13:
                    name = 'Король'
                else:
                    name = 'Туз'

            self.__deck.append(Card(name, 'черви'))
            self.__deck.append(Card(name, 'крести'))
            self.__deck.append(Card(name, 'пики'))
            self.__deck.append(Card(name, 'бубны'))

            shuffle(self.__deck)
