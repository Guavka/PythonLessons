from typing import Any, Generic, List, Callable
# Модуль typing нужен для аннотаций сложных типов данных


def check_arguments_type(check_funcs: List[Callable]) -> Any:
    """
    Декоратор, который проверяет функции на соответствие входных данных аннотации (тип данных в аннотации = тип данных параметра), 
    а также проверяет исходящее значение согласно аннотации

    Args:
        check_funcs (List[Callable]): Список функций-проверок, которые вызываются перед вызовом основной функции 
    """
    def decorator(fn: Callable) -> Any:
        def wrapper(*args, **kwargs) -> Any:
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
    """Функция - проверка на то, что границы проходят валидацию

    Args:
        number1 (int): Левая граница
        number2 (int): Правая граница

    Exceptions:
        AssertationError
    """
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
    print(result)
except Exception as ex:
    print(ex)
