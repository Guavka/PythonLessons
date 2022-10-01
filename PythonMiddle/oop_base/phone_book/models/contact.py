
from typing import Dict
from models.phone import Phone, PhoneSettings

from utils.validator import isValidName


class Contact:
    """
Класс, который хранит в себе информацию об 1 контакте.
Имя контакта - строка, не пустая, начинается не с цифры
Словарь контактов - словарь, состоящий из объектов класса Phone, а ключ - их имена
    """

    __first_name: str = ''
    __last_name: str = ''
    __second_name: str = ''
    __numbers: Dict[str, Phone] = {}

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        isValidName(value=value,
                    type_err_msg='Имя должно быть строкой',
                    empty_err_msg='Поле "Имя" пустое',
                    len_err_msg='Поле "Имя" должно занимать смволов в диапазоне',
                    only_number_err_msg='Имя не может состоять только из чисел',
                    start_number_err_msg='Имя должно начинаться не с цифры')

        self.__first_name = value

    @property
    def second_name(self):
        return self.__second_name

    @second_name.setter
    def second_name(self, value: str):
        isValidName(value=value,
                    type_err_msg='Отчество должно быть строкой',
                    empty_err_msg='Поле "Отчество" пустое',
                    len_err_msg='Поле "Отчество" должно занимать смволов в диапазоне',
                    only_number_err_msg='Отчество не может состоять только из чисел',
                    start_number_err_msg='Отчество должно начинаться не с цифры')

        self.__second_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        isValidName(value=value,
                    type_err_msg='Фамилия должно быть строкой',
                    empty_err_msg='Поле "Фамилия" пустое',
                    len_err_msg='Поле "Фамилия" должно занимать смволов в диапазоне',
                    only_number_err_msg='Фамилия не может состоять только из чисел',
                    start_number_err_msg='Фамилия должно начинаться не с цифры')

        self.__last_name = value

    @first_name.setter
    def first_name(self, value: str):
        isValidName(value=value,
                    type_err_msg='Имя должно быть строкой',
                    empty_err_msg='Поле "Имя" пустое',
                    len_err_msg='Поле "Имя" должно занимать смволов в диапазоне',
                    only_number_err_msg='Имя не может состоять только из чисел',
                    start_number_err_msg='Имя должно начинаться не с цифры')

        self.__first_name = value

    @property
    def numbers(self):
        from copy import deepcopy
        return deepcopy(self.__numbers)

    def add_number(self, number: Phone):
        assert isinstance(number, Phone), 'Неверный формат номера'

        assert not (number.name in self.__numbers), 'Данное имя уже занято'

        self.__numbers[number.name] = number

    def remove_number(self, number: Phone):
        assert isinstance(number, Phone), 'Неверный формат номера'
        self.__numbers[number.name] = None

    def __init__(self, first_name: str, second_name: str = None, last_name: str = None, numbers: Dict[str, Phone] = None) -> None:
        self.first_name = first_name
        
        if not second_name is None:
            self.second_name = second_name
        if not last_name is None:
            self.last_name = last_name
        if not last_name is None:
            self.numbers = numbers
