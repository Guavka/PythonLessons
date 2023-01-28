# Функции - механизм по разделению кода на логические части


'''
def имя_функции(параметры_функции):
    тело функции
'''

# Без функции
result = 0
for number in range(1, 5 + 1):
    result += number
print(result)

# Без функции (новый диапазон)
result = 0
for number in range(3, 8 + 1):
    result += number
print(result)


def print_range_sum(left_edge, right_edge):
    result = 0
    for number in range(left_edge, right_edge + 1):
        result += number
    print(result)


print_range_sum(1, 5)
print_range_sum(3, 8)
print_range_sum(11, 15)


def get_range_sum(left_edge, right_edge):
    result = 0
    for number in range(left_edge, right_edge + 1):
        result += number
    return result


result = get_range_sum(1, 5) + get_range_sum(3, 8)

# Анонимные функции

'''
result = lambda параметры: тело_функции
'''


def sqr(number):
    return number**2


result = sqr(15)
print(result)


def sqr2(number): return number**2


result = sqr2(15)
print(result)


def power(number, power):
    return number**power


result = power(15, 2)
print(result)


def power2(number, power): return number**power


result = power2(15, 2)
print(result)

result = sqr(15)
print(result)
result = (lambda i: i**2)(15)
print(result)


# Добавляем аннотации


def get_range_sum(left_edge: int, right_edge: int) -> int:
    result = 0
    for number in range(left_edge, right_edge + 1):
        result += number
    return result

# Добавляем описание


def print_range_sum(left_edge: int, right_edge: int)->None:
    """
    Функция, которая считает и выводит в консоль сумму чисел в диапазоне
     Args:
        left_edge (int): Левая граница
        right_edge (int): Правая граница
    """
    
    result = 0
    for number in range(left_edge, right_edge + 1):
        result += number
    print(result)


def get_range_sum(left_edge: int, right_edge: int) -> int:
    """
    Функция, которая считает и возвращает сумму чисел в диапазоне
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

'''
args и kwargs

args - набор из параметров, которые переданы по порядку
kwargs - набор из параметров, которые переданы по контексту
'''


def get_division(number1: int, number2: int) -> float:
    return number1/number2


result = get_division(10, 2)  # args
print(result)
result = get_division(number2=2, number1=10)  # kwargs
print(result)


def print_name(name: str, last_name: str, nick='User123', is_active=True):
    print(f'Name: {name}\n\
Last name: {last_name}\n\
Nick: {nick}\n\
Is active: {is_active}')


# Только args - все по порядку, все нужны
print_name('Alex', 'Smirnov')
print_name('Alex', 'Smirnov', 'Guavka')
print_name('Alex', 'Smirnov', 'User123', False)

# Только kwargs - name, last_name - обязательные, is_active - необязательный
print_name(name='Alex',
           last_name='Smirnov',
           is_active=False)


# Гибрид - и то, и то
print_name('Alex', 'Smirnov', is_active=False)
