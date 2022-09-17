# Функции - механизм по разделению кода на логические части


'''
def имя_функции(параметры_функции):
    тело функции
'''


def print_range_sum(left_edge: int, right_edge: int):
    """Функция, которая считает и выводит в консоль сумму чисел в диапазоне

    Args:
        left_edge (int): Левая граница
        right_edge (int): Правая граница
    """
    result = 0
    for number in range(left_edge, right_edge + 1):
        result += number
    print(result)


def get_range_sum(left_edge: int, right_edge: int) -> int:
    """Функция, которая считает и возвращает сумму чисел в диапазоне

    Args:
        left_edge (int): Левая граница
        right_edge (int): Правая граница

    Returns:
        int: сумма чисел в диапазоне
    """
    result = 0
    for number in range(left_edge, right_edge + 1):
        result += number
    return result


print_range_sum(2, 4)

result = get_range_sum(2, 4) + get_range_sum(1, 8)
print(result)
