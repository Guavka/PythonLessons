'''
1. Вывод на экран меню
2. Выбор из списка напитков
3. Выбор объема из списка
4. Выбор количества сахара 
5. Выбор добавок
6. Расчет суммы
'''


from typing import Literal


def get_coffee_order():
    drink_dict = {
        'кофе': {
            200: 100,
            300: 150,
            400: 200
        },
        'чай': {
            200: 80,
            300: 100,
            400: 120
        },
        'латте': {
            200: 120,
            300: 170,
            400: 220
        },
    }

    add_dict = {
        'лимон': 5,
        'молоко': 20,
        'корица': 10,
        'ничего': 0
    }

    def get_drink() -> Literal['кофе', 'чай', 'латте'] | None:
        """Функция, которая выводит на экран список напитков и просит сделать выбор.

        Returns:
            Literal['кофе', 'чай', 'латте'] | None: выбранный напиток или "отмена"
        """
        while True:
            user_choose = input(
                'Привет!\nВыбери напиток:\n1.Кофе\n2.Чай\n3.Латте\n4.Выход\n')
            if user_choose == '1':
                return 'кофе'
            elif user_choose == '2':
                return 'чай'
            elif user_choose == '3':
                return 'латте'
            elif user_choose == '4':
                return None
            else:
                print('Введи число от 1 до 4')

    def get_volume():
        """Функция, которая выводит на экран список объемов и просит сделать выбор.

        Returns:
            Literal[200, 300, 400] | None: выбранный объем или "отмена"
        """
        while True:
            user_choose = input(
                'Выбери объем:\n1.200мл\n2.300мл\n3.400мл\n4.Выход\n')
            if user_choose == '1':
                return 200
            elif user_choose == '2':
                return 300
            elif user_choose == '3':
                return 400
            elif user_choose == '4':
                return None
            else:
                print('Введи число от 1 до 4')

    def get_sugar():
        """Функция, которая просит выбрать количество сахара (от 0 до 5)

        Returns:
            int: количество сахара
        """
        while True:
            user_choose = input(
                'Выбери количество сахара от 0 до 5 или "выход": ')
            if user_choose == 'выход':
                return None

            try:
                user_choose = int(user_choose)
            except:
                print('Вы должны ввести число!')
            else:
                try:
                    assert user_choose in range(
                        0, 5+1), 'Количество сахара должно быть в диапазоне от 0 до 5'
                    return user_choose
                except AssertionError as ex:
                    print(ex)

    def get_add():
        """Функция, которая выводит на экран список добавок и просит сделать выбор.

        Returns:
            list | None: выбранная добавка или "отмена"
        """
        
        add_list =[]
        
        while True:
            user_choose = input(
                'Привет!\nВыбери напиток:\n1.Лимон\n2.Молоко\n3.Корица\n4.Не нужно(Хватит)\n5.Выход\n')
            if user_choose == '1':
                add_list.append('лимон')
            elif user_choose == '2':
                add_list.append('молоко')
            elif user_choose == '3':
                add_list.append('корица')
            elif user_choose == '4':
                return add_list
            elif user_choose == '5':
                return None
            else:
                print('Введи число от 1 до 4')

    def calculate_sum(drink: str, volume: int, sugar: int, add_list: str):
        """Функция, которая генерирует финальный заказ

        Args:
            drink (str): выбранынй напиток
            volume (int): объем
            sugar (int): количество сахара
            add (str): добавки

        Returns:
            _type_: счет
        """
        # цена напитка в зависимости от объема
        drink_sum = drink_dict[drink][volume]
        
        add_sum = 0
        for add in add_list:
            add_sum += add_dict[add]

        return {
            'drink': drink,
            'volume': volume,
            'sugar': sugar,
            'drink_sum': drink_sum,
            'add_sum': add_sum,
            'result': drink_sum + add_sum
        }

    drink = get_drink()
    if drink is None:
        return None

    volume = get_volume()
    if volume is None:
        return None

    sugar = get_sugar()
    if sugar is None:
        return None

    add = get_add()
    if add is None:
        return None

    return calculate_sum(drink=drink, volume=volume, sugar=sugar, add_list=add)
