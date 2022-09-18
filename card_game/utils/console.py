
def get_data(msg: str = 'Input value:', user_type: type = int):
    """Функция, которая считывает с консоли значение и пытается его предобразовать в тип данных, указанный пользователем

    Args:
        msg (str, optional): Сообщение пользователя. Defaults to 'Input value:'.
        user_type (type, optional): Тип даанных, ожидаемый пользователем. Defaults to int.

    Returns:
        (user_type|None): результат
    """
    value = input(f'{msg} ')
    try:
        value = user_type(value)
    except Exception as ex:
        print(ex)
    else:
        return value


def get_data_infinite(msg: str = 'Input value:', user_type: type = int):
    """Функция, которая считывает с консоли значение в бесконечном цикле и пытается его предобразовать в тип данных, указаннынй пользователем

    Args:
        msg (str, optional): Сообщение пользователя. Defaults to 'Input value:'.
        user_type (type, optional): Тип даанных, ожидаемый пользователем. Defaults to int.

    Returns:
        (user_type|None): результат
    """
    while True:
        result = get_data(msg=msg, user_type=user_type)
        if result != None:
            return result


def print_data(msg: str):
    print(f'[INFO] {msg}')

