'''
1. Вывод на экран меню
2. Выбор из списка напитков
3. Выбор объема из списка
4. Выбор количества сахара 
5. Выбор добавок
6. Расчет суммы
'''
from typing import Callable


def get_coffee_order(drink_dict: dict, add_dict: dict, output_fn: Callable, input_fn: Callable):
    from typing import Collection

    def print_menu(collection: Collection, start_msg: str, postfix: str = ''):
        """Функция, которая выводит на экран меню из списка

        Args:
            collection (Collection): коллекция, в которой перечислено меню
            start_msg (str): стартовое сообщение
        """
        output_fn(start_msg)

        index = 1
        for item in collection:
            output_fn(f'{index}.{str(item).capitalize()}{postfix}')  # aaaa - Aaaa
            index += 1

        output_fn(f'{index}.Выход')

    def input_menu_item(collection: list, input_msg: str):
        """Функция, которая просит ввести число согласно коллекции.

        Args:
            collection (list): список из данных
            input_msg (str): сообщение при вводе

        Returns:
            Any | None: Any - значение из списка согласно введенному значению, None - пользователь нажал "отмена"
        """
        exit_index = len(collection)
        while True:
            user_choose = input_fn(input_msg)
            try:
                user_choose = int(user_choose) - 1
                assert 0 <= user_choose <= exit_index
            except AssertionError:
                output_fn(f'Число должно быть в диапазоне [1,{exit_index+1}]')
            except Exception:
                output_fn('Неверный формат числа')
            else:
                return None if user_choose == exit_index else collection[user_choose]

    def get_drink():
        """Функция, которая выводит на экран список напитков и просит сделать выбор.

        Returns:
            Any | None: выбранный напиток или "отмена"
        """

        drink_list = list(drink_dict.keys())
        print_menu(start_msg='Привет!',
                   collection=drink_list)

        return input_menu_item(input_msg='Выбери напиток:',
                               collection=drink_list)

    def get_volume(choosed_drink: dict):
        """Функция, которая выводит на экран список объемов и просит сделать выбор.

        Args:
           choosed_drink (dict): информация об объемах выбранногго напитка

        Returns:
            int | None: выбранный объем или "отмена"
        """

        volume_list = list(choosed_drink.keys())
        print_menu(start_msg='Теперь выберите объем.',
                   collection=volume_list,
                   postfix='мл')

        return input_menu_item(input_msg='Выбери объем:',
                               collection=volume_list)

    def get_sugar():
        """Функция, которая просит выбрать количество сахара (от 0 до 5)

        Returns:
            int: количество сахара
        """

        sugar_list = list(range(0, 5))
        print_menu(start_msg='Теперь выберите количество сахара',
                   collection=sugar_list,
                   postfix=' ложка')

        return input_menu_item(input_msg='Выбери сахар:',
                               collection=sugar_list)

    def get_add():
        """Функция, которая выводит на экран список добавок и просит сделать выбор.

        Returns:
            list | None: выбранная добавка или "отмена"
        """

        nothing_val = 'Достаточно'
        adds_list = list(add_dict.keys()) + [nothing_val]
        add_list = []
        while True:
            print_menu(start_msg='Теперь выберите добавки.',
                       collection=adds_list)

            result = input_menu_item(input_msg='Выбери добавки:',
                                     collection=adds_list)
            if result is None:
                return None

            if result == nothing_val:
                return add_list

            add_list.append(result)

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

    drink_name = get_drink()
    if drink_name is None:
        return None

    volume = get_volume(drink_dict[drink_name])
    if volume is None:
        return None

    sugar = get_sugar()
    if sugar is None:
        return None

    add = get_add()
    if add is None:
        return None

    return calculate_sum(drink=drink_name, volume=volume, sugar=sugar, add_list=add)
