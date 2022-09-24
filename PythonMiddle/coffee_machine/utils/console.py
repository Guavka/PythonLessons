from typing import Collection


def show_menu_from_collection(collection: Collection, start_message: str = 'Input data:', isMenu=True):
    while True:
        if isMenu:
            print_menu_from_list(data=collection,
                                 isExit=True,
                                 message=start_message)
        else:
            print(start_message)
        user_choose = input()

        try:
            user_choose = int(user_choose)
        except:
            print('Вы ввели не число!')
        else:
            length = len(collection) + 1
            try:
                assert user_choose in range(
                    1, length+1), f'Число должно быть в диапазоне от 1 до {length}'
            except AssertionError as ex:
                print(ex)
            else:
                if user_choose == length:
                    return None

                if type(collection) == dict:
                    collection = list(collection.keys())

                return collection[user_choose-1]


def print_menu_from_list(data: Collection, counter: int = 1, isCountered=True, isExit=False, message: str = 'Input data:'):
    print(f'{message} ')
    i = counter
    for value in data:
        if isCountered:
            print(f'{i}.{str(value).capitalize()}')
            i += 1
        else:
            print(f'{str(value).capitalize()}')
    if isExit:
        if isCountered:
            print(f'{i}.Выход')
        else:
            print('Выход')
