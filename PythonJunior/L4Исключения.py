# Исключения - механизм по контролю ошибок. Рзличают внутренние исключения и те, которые вызвал програмист

print('----------Отлов исключений-----------')
'''
Отлов исключений

try:
    код_который_тестируется
except Exception as ex:
    код_при_ошибке
'''

number1 = 5
number2 = None

try:
    print(number1 / number2)
except Exception as ex:
    print(ex)

'''
try:
    код_который_тестируется
except Exception as ex:
    код_при_ошибке
else:
    код_если все хорошо
'''

number1 = 5
number2 = 2

try:
    print(number1 / number2)
except Exception as ex:
    print(ex)
else:
    print('Успех!')

'''
try:
    код_который_тестируется
except класс_ошибки as ex:
    код_при_ошибке
except Exception as ex:
    код_при_ошибке
'''

number1 = 5
number2 = None

try:
    print(number1 / number2)
except TypeError:
    print('Странные типы данных!')
except ZeroDivisionError:
    print('Ты поделил на 0, а так нельзя!')
except Exception as ex:
    print(ex)

'''
try:
    код_который_тестируется
except Exception as ex:
    код_при_ошибке
finally:
    код_в_любом_случае
'''

number1 = 5
number2 = 2

try:
    print(number1 / number2)
except ZeroDivisionError:
    print('Ты поделил на 0, а так нельзя!')
except Exception as ex:
    print(ex)
finally:
    print('Соединение закрыто')

print('----------Вызов(бросание) исключений-----------')

'''
if условие:
    raise класс_ошибки(сообщение)
'''

age = -5
try:  # *** - хорошо
    if age < 0:
        raise AttributeError('age должен быть больше 0')
except AttributeError as ex:
    print(ex)

try:
    if age < 0:
        raise AttributeError()
except AttributeError:
    print('age должен быть больше 0')

'''
assert

assert условие, сообщение 
'''

age = -5
try:
    assert age >= 0, 'age должен быть больше 0'
except AssertionError as ex:
    print(ex)
