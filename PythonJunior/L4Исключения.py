
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
number2 = 0

try:
    print(number1 / number2)
except Exception as ex:
    print(ex)
    
while True:
    number = input('Введи число 5: ')
    try:
        number = int(number)
    except Exception as ex:
        print(ex)
    if number == 5:
        break

print('----------Конструкция try .. else-----------')  
'''
try:
    код_который_тестируется
except Exception as ex:
    код_при_ошибке
else:
    код_если все хорошо
'''

number1 = 5
number2 = 0

try:
    print(number1 / number2)
except Exception as ex:
    print(ex)
else:
    print('Успех!')
    

print('----------Отлов исключений различного типа-----------')    
'''
try:
    код_который_тестируется
except класс_ошибки as ex:
    код_при_ошибке
except Exception as ex:
    код_при_ошибке
'''

number1 = 5
number2 = 'ноль'

try:
    print(number1 / number2)
except TypeError:
    print('Странные типы данных!')
except ZeroDivisionError:
    print('Ты поделил на 0, а так нельзя!')
except Exception as ex:
    print(ex)
    
print('----------finally-----------')  
'''
try:
    код_который_тестируется
except Exception as ex:
    код_при_ошибке
finally:
    код_в_любом_случае
'''

number1 = 5
number2 = 0

try:
    print(number1 / number2)
except ZeroDivisionError:
    print('Ты поделил на 0, а так нельзя!')
except Exception as ex:
    print(ex)
finally:
    print('Соединение закрыто')
    
try:
    print(number1 / number2)
except ZeroDivisionError:
    print('Ты поделил на 0, а так нельзя!')
except Exception as ex:
    print(ex)
print('Соединение закрыто')

print('----------Вызов(бросание) исключений-----------')

print('----------Raise-----------')
'''
if условие:
    raise класс_ошибки(сообщение)
'''

age = -5
try:  # при нескольких одинаковых типах ошибки
    if age < 0:
        raise AttributeError('age должен быть больше 0')
except AttributeError as ex:
    print(ex)

try: # при условии, что данная ошибка встретится 1 раз
    if age < 0:
        raise AttributeError()
except AttributeError:
    print('age должен быть больше 0')
    
    
age = 155

try:
    if age < 0:
        raise AttributeError('age должен быть больше 0')
    elif age > 150:
        raise AttributeError('age должен быть меньше 150')
except Exception as ex:
    print(ex)

try:
    if age < 0:
        raise AttributeError()
    elif age > 150:
        raise AttributeError()
except Exception:
    print('age должен быть больше 0 и меньше 150')
    

print('----------Assert-----------')   
'''
assert условие, сообщение_если_условие_не_выполнилось
'''

age = -5
try:
    assert age > 0, 'age должен быть больше 0'
except AssertionError as ex:
    print(ex)
