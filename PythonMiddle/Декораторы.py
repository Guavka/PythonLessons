'''
Декораторы - механизм языка, который позволяет перед вызовом функции вызвать другую функцию. Работает по принципу обертки.
'''


def test_dec(fn):
    def wrapper():
        print('Decorator')
        fn()
    return wrapper


@test_dec
def hello():
    print('hello')


hello()

'''
Декоратор функции с параметрами
'''


def check_int_range(fn):
    def wrapper(number1: int, number2: int):
        assert type(number1) == int, 'Аргумент "number1" должен быть int'
        assert type(number2) == int, 'Аргумент "number2" должен быть int'
        assert number1 < number2, 'Левая граница должна быть меньше правой'

        return fn(number1, number2)
    return wrapper


@check_int_range
def get_range_sum_annotation_docs_check_decorated(number1: int, number2: int) -> int:
    """Функция, которая считает и возвращает сумму чисел в диапазоне

    Args:
        number1 (int): Левая граница
        number2 (int): Правая граница

    Returns:
        int: Сумма чисел от "Левая граница" до "Правая граница"
    """

    result = 0
    for number in range(number1, number2 + 1):
        result += number
    return result


try:
    result = get_range_sum_annotation_docs_check_decorated(2, 4)
except Exception as ex:
    print(ex)
else:
    print(result)


'''
Декоратор с аргументами
'''


def check_int_range(is_print: bool):
    def decorator(fn: Callable):
        def check_types(number1: int, number2: int):
            assert type(number1) == int, 'Аргумент "number1" должен быть int'
            assert type(number2) == int, 'Аргумент "number2" должен быть int'
            assert number1 < number2, 'Левая граница должна быть меньше правой'

            result = fn(number1, number2)
            result_type = fn.__annotations__['return']

            assert type(
                result) == result_type, 'Функция возвращает значение не того типа!'

            if is_print:
                print(result)
            return result
        return check_types
    return decorator


@check_int_range(is_print=True)
def get_range_sum_annotation_docs_check_decorated(number1: int, number2: int) -> int:
    """Функция, которая считает и возвращает сумму чисел в диапазоне

    Args:
        number1 (int): Левая граница
        number2 (int): Правая граница

    Returns:
        int: Сумма чисел от "Левая граница" до "Правая граница"
    """

    result = 0
    for number in range(number1, number2 + 1):
        result += number
    return result


try:
    result = get_range_sum_annotation_docs_check_decorated(2, 4)
except Exception as ex:
    print(ex)

'''
Универсальный декоратор с аргументами
'''


def check_type(is_print: bool):
    def decorator(fn: Callable):
        def check_types(*args, **kwargs):
            '''
                args = [2,4]
                kwargs = {
                    'number1': 2,
                    'number2': 4,
                }
                fn.__annotations__ = {
                    'number1': <class 'int'>, 
                    'number2': <class 'int'>, 
                    'return': <class 'int'>
                }
            '''

            for key in kwargs:
                type_value = fn.__annotations__[key]
                assert isinstance(
                    kwargs[key], type_value), f'Аргумент "{key}" должен быть {type_value}'

            number1, number2 = kwargs['number1'], kwargs['number2']
            assert number1 < number2, 'Левая граница должна быть меньше правой'

            result = fn(number1, number2)
            result_type = fn.__annotations__['return']

            assert type(
                result) == result_type, 'Функция возвращает значение не того типа!'

            result = fn(*args, **kwargs)
            if is_print:
                print(result)
            return result
        return check_types
    return decorator


@check_type(is_print=True)
def get_range_sum_annotation_docs_check_decorated_universal(number1: int, number2: int) -> int:
    """Функция, которая считает и возвращает сумму чисел в диапазоне

    Args:
        number1 (int): Левая граница
        number2 (int): Правая граница

    Returns:
        int: Сумма чисел от "Левая граница" до "Правая граница"
    """

    result = 0
    for number in range(number1, number2 + 1):
        result += number
    return result


try:
    result = get_range_sum_annotation_docs_check_decorated_universal(
        number1=2, number2=4)
except Exception as ex:
    print(ex)


'''
Декоратор с возможностью добавления дополнительных проверок
'''


def check_arguments_type(check_funcs: List[Callable]):
    def decorator(fn: Callable):
        def wrapper(*args, **kwargs):
            assert len(
                kwargs.keys()) != 0, 'kwargs пустой - используйте имя_параметра=значение при вызове функции\nexample(number=10)'
            assert len(
                fn.__annotations__.keys()) != 0, '__annotations__ пустой - что-то пошло не так при вызове'

            for key in kwargs:
                type_value = fn.__annotations__[key]
                assert isinstance(
                    kwargs[key], type_value), f'Аргумент "{key}" должен быть {type_value}'

            for func in check_funcs:
                func(*args, **kwargs)

            result = fn(*args, **kwargs)
            result_type = fn.__annotations__['return']
            assert isinstance(
                result, result_type), f'return должен быть {result_type}'

            return result
        return wrapper
    return decorator


def check_edges(number1: int, number2: int):
    assert number1 < number2, 'Левая граница должна быть меньше правой'


@check_arguments_type([check_edges])
def get_range_sum(number1: int, number2: int) -> int:
    """Функция, которая считает и возвращает сумму чисел в диапазоне

    Args:
        number1 (int): Левая граница
        number2 (int): Правая граница

    Returns:
        int: Сумма чисел от "Левая граница" до "Правая граница"
    """

    result = 0
    for number in range(number1, number2 + 1):
        result += number
    return result


try:
    result = get_range_sum(number1=2, number2=4)
except Exception as ex:
    print(ex)
