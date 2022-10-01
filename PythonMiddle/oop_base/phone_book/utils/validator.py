def isValidStr(value: str, type_err_msg: str = 'not string', empty_err_msg: str = 'is empty'):
    """Функция, которая проверяет значение на то, что это строка и она не пустая

    Args:
        value (str): значение
        type_err_msg (str): Сообщение, если это не строка
        empty_err_msg (str): Сообщение, если строка пустая
    """
    assert type(value) == str, type_err_msg
    assert value != '', empty_err_msg


def isValidPhoneNumber(value: str,
                       type_err_msg = 'not string',
                       empty_err_msg = 'is empty',
                       letters_err_msg = 'need no letters',
                       len_err_msg = 'not correct len'):
    """Функция валидации телефонных номеров

    Args:
        value (str): значение для проверки
        type_err_msg (str, optional): Сообщение при неверном типе данных. Defaults to 'not string'.
        empty_err_msg (str, optional): Сообщение, если строка пустая. Defaults to 'is empty'.
        letters_err_msg (str, optional): Сообщение, если в номере есть буквы . Defaults to 'need no letters'.
        len_err_msg (str, optional): Сообщение, если в номере меньше или больше цифр. Defaults to f'not correct numbers'.
    """
    isValidStr(value=value,
               type_err_msg=type_err_msg,
               empty_err_msg=empty_err_msg)

    length = 10
    test_value = value
    if value[0] == '+':
        length = 11
        test_value = test_value[1::]

    assert test_value.isnumeric(), letters_err_msg
    assert len(
        test_value) == length, f'{len_err_msg} {length}'


def isValidName(value: str,
                type_err_msg = 'not string',
                empty_err_msg = 'is empty',
                start_number_err_msg = 'no start with number',
                only_number_err_msg = 'not only numbers',
                len_err_msg = 'not correct len',
                min_len = 4,
                max_len=15):
    """Функция валидации имени

    Args:
        value (str): Значение
        type_err_msg (str, optional): Сообщение, если это не строка. Defaults to 'not string'.
        empty_err_msg (str, optional): Сообщение, если строка пустая. Defaults to 'is empty'.
        start_number_err_msg (str, optional): Сообщение, если начинается с числа. Defaults to 'no start with number'.
        only_number_err_msg (str, optional): Сообщение, если строка состоит только из чисел. Defaults to 'not only numbers'.
        len_err_msg (str, optional): Сообщение, если строка неверной длины. Defaults to 'not correct len'.
        min_len (int, optional): Минимальная длина. Defaults to 4.
        max_len (int, optional): Максимальная длина. Defaults to 15.
    """
    
    isValidStr(value=value,
               type_err_msg=type_err_msg,
               empty_err_msg=empty_err_msg)

    assert min_len <= len(
        value) <= max_len, f'{len_err_msg} [{min_len},{max_len}]'
    assert not value.isnumeric(), only_number_err_msg
    assert not value[0].isnumeric(), start_number_err_msg
