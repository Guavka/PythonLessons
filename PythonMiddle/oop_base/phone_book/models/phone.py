
from dataclasses import dataclass
from utils.validator import isValidName, isValidPhoneNumber


@dataclass
class PhoneSettings:
    """
    Класс настроек для класс Phone
    """
    name: str
    number: str


class Phone:
    """
    Класс "Телефон". Хранит в себе название и номер телефона.
Название должно быть строкой и не пустое
Телефон должен быть строкой и либо начинаться с + и 11 символов (+79490001122) либо 10 символов (9490001122)
    """
    __name = ''
    __number = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        isValidName(value=value,
                    type_err_msg='Имя должно быть строкой',
                    empty_err_msg='Поле "Имя" пустое',
                    len_err_msg='Поле "Имя" должно занимать смволов в диапазоне',
                    only_number_err_msg='Имя не может состоять только из чисел',
                    start_number_err_msg='Имя должно начинаться не с цифры')

        self.__name = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value: str):
        isValidPhoneNumber(value=value,
                           type_err_msg='Номер должно быть строкой',
                           empty_err_msg='Поле "Номер" пустое',
                           letters_err_msg='В номере телефона не должно быть букв',
                           len_err_msg='неверное количество символов. Нужно: ')

        self.__number = value

    def __init__(self, settings: PhoneSettings) -> None:
        assert isinstance(settings, PhoneSettings), 'Объект настроек неверен'

        self.name = settings.name
        self.number = settings.number

    def __str__(self) -> str:
        return f'Name: {self.name}\nNumber: {self.number}'
