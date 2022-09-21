'''
Алгоритм

1. Приветствие (меню)
2. Выбор напитка (кофе, чай, латте)
3. Сахар (от 0 до 5)
4. Добавки (лимон, молоко)
5. Расчет суммы
6. Получение денег
7. Получение напитка
'''


def coffee_machine():
    """
    Основная функция кофемашины, вызывает внутренние функции и возращает либо None(пользователь отказался) либо True(оплата прошла).

    returns 
    None - пользователь отказался
    True - оплата прошла
    """
    def menu():
        """
        Выбор напитка

        Returns:
            str | None: выбранный напиток
        """
        while True:
            print('Welcome!\nChoose drink:\n 1.Coffee\n 2.Tea\n 3.Latte\n 4.Exit')
            user_choose = input('Input menu item: ')
            if user_choose == '1':
                return 'coffee'
            elif user_choose == '2':
                return 'tea'
            elif user_choose == '3':
                return 'latte'
            elif user_choose == '4':
                return None
            else:
                print('Error! Input number in range [1,4]')

    def get_volume():
        """
        Выбор объема (влияет на цену)

        Returns:
            str | None: выбранный объем
        """
        while True:
            print('Choose volume:\n 1.Small\n 2.Medium\n 3.Big\n 4.Exit')
            user_choose = input('Input number: ')
            if user_choose == '1':
                return 200
            elif user_choose == '2':
                return 300
            elif user_choose == '3':
                return 400
            elif user_choose == '4':
                return None
            else:
                print('Error! Input number in range [1,4]')

    def get_sugar():
        """
        Выбор количества сахара (не влияет на цену)

        Returns:
            str | None: выбранное количество сахара
        """
        while True:
            print('Choose sugar from 0 to 5 or -1 for "Exit":')
            user_choose = input('Input number: ')

            try:
                user_choose = int(user_choose)
            except:
                print('Error data! Input only numbers!')
            else:
                if user_choose == -1:
                    return None
                elif user_choose in range(0, 5+1):
                    return user_choose
                else:
                    print('Error! Input number in range [0,5]')

    def calculate(drink: str, volume: int):
        """Функция расчета стоимости на основании напитка и объема

        Args:
            drink (str): Выбранный напиток
            volume (int): Выбранный объем

        Returns:
            _type_: стоимость
        """
        result_sum: int = 0
        if drink == 'coffee':
            result_sum += 100
        elif drink == 'tea':
            result_sum += 80
        elif drink == 'latte':
            result_sum += 150

        if volume == 300:
            result_sum *= 1.2
        elif volume == 400:
            result_sum *= 1.5

        return result_sum

    def get_money(price: int):
        """Функция расчета пользователя с системой

        Args:
            price (int): Цена

        Returns:
            _type_: Успешна ли операция
        """
        while True:
            print(f'Finale sum: {price}')
            while True:
                user_money = input('Input money sum or "exit": ')
                if user_money == 'exit':
                    return False
                try:
                    user_money = int(user_money)
                except:
                    print('Input only number!')
                else:
                    break
            if user_money == price:
                print('Have a nice day!')
                return True
            elif user_money > price:
                print(f'Your sum: {user_money-price}')
                print('Have a nice day!')
                return True
            else:
                print('Need more money!')

    while True:
        drink = menu()  # 'coffee' | 'tea'| 'latte'| None
        if drink is None:
            return

        volume = get_volume()  # 200| 300| 400| None
        if volume is None:
            return

        sugar = get_sugar()  # 0-5 | None
        if sugar is None:
            return

        result = calculate(drink, volume)

        return get_money(result)
