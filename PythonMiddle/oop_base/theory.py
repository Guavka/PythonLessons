import dataclasses
from re import A


user_dict = {
    'User1': {
        'login': 'User1',
        'pass': '123123',
        'age': 25
    },
    'User2': {
        'login': 'User2',
        'pass': '123123',
        'ag': 25
    },
}


class User:
    login = 'User1'
    password = '123123'
    age = 25


user = User()
user.login = 4

print(user.login)

# ------------Private


class PrivateUser():
    # Private поля - защищены от доступа из вне
    __login = 'User1'
    __password = '123123'
    __age = 25

    def print_user(self):
        print(self.__login, self.__password, self.__age)


user = PrivateUser()
user.__age = 15
user.print_user()

# --------------Properties


class PropertyReadUser():
    # Private поля - защищены от доступа из вне
    __login = 'User1'
    __password = '123123'
    __age = 25

    @property
    def login(self):  # функция чтения из поля __login
        return self.__login

    @property
    def password(self):  # функция чтения из поля __password
        return self.__password

    @property
    def age(self):  # функция чтения из поля __age
        return self.__age

    def print_user(self):
        print(self.__login, self.__password, self.__age)


user = PropertyReadUser()


class PropertyUser():
    # Private поля - защищены от доступа из вне
    __login = 'User1'
    __password = '123123'
    __age = 25

    @property
    def login(self):  # функция чтения из поля __login
        return self.__login

    @login.setter
    def login(self, value: str):
        assert type(value) == str, 'Логин должен быть строкой'
        assert value != '', 'Поле "Логин" пустое'
        assert 4 <= len(
            value) <= 15, 'Поле "Логин" должно занимать от 4 до 15 символов'
        assert not value.isnumeric(), 'Логин не может состоять только из чисел'

        self.__login = value

    @property
    def password(self):  # функция чтения из поля __password
        return self.__password

    @password.setter
    def password(self, value: str):
        assert type(value) == str, 'Пароль должен быть строкой'
        assert value != '', 'Поле "Пароль" пустое'
        assert 6 <= len(
            value) <= 15, 'Поле "Пароль" должно занимать от 6 до 15 символов'

        self.__password = value

    @property
    def age(self):  # функция чтения из поля __age
        return self.__age

    @age.setter
    def age(self, value: int):
        assert type(value) == int, 'Возраст должен быть числом'
        assert 0 < value <= 120, 'Возраст должен быть от 1 до 120'

        self.__age = value

    def print_user(self):
        print(self.__login, self.__password, self.__age)


user = PropertyUser()
user.login = 'Test1'
user.password = '1234123235'
user.age = 15

# --------------------Constructor


class UserConstructor():
    # Private поля - защищены от доступа из вне
    __login = 'User1'
    __password = '123123'
    __age = 25

    @property
    def login(self):  # функция чтения из поля __login
        return self.__login

    @login.setter
    def login(self, value: str):
        assert type(value) == str, 'Логин должен быть строкой'
        assert value != '', 'Поле "Логин" пустое'
        assert 4 <= len(
            value) <= 15, 'Поле "Логин" должно занимать от 4 до 15 символов'
        assert not value.isnumeric(), 'Логин не может состоять только из чисел'

        self.__login = value

    @property
    def password(self):  # функция чтения из поля __password
        return self.__password

    @password.setter
    def password(self, value: str):
        assert type(value) == str, 'Пароль должен быть строкой'
        assert value != '', 'Поле "Пароль" пустое'
        assert 6 <= len(
            value) <= 15, 'Поле "Пароль" должно занимать от 6 до 15 символов'

        self.__password = value

    @property
    def age(self):  # функция чтения из поля __age
        return self.__age

    @age.setter
    def age(self, value: int):
        assert type(value) == int, 'Возраст должен быть числом'
        assert 0 < value <= 120, 'Возраст должен быть от 1 до 120'

        self.__age = value

    def __init__(self, login: str, password: str, age: int) -> None:
        # 1 раз при создании объекта
        self.login = login
        self.password = password
        self.age = age

    def print_user(self):
        print(self.__login, self.__password, self.__age)


@dataclasses.dataclass
class UserSettings():
    login: str
    password: str
    age: int


class UserObject():
    # Private поля - защищены от доступа из вне
    __login = 'User1'
    __password = '123123'
    __age = 25

    @property
    def login(self):  # функция чтения из поля __login
        return self.__login

    @login.setter
    def login(self, value: str):
        assert type(value) == str, 'Логин должен быть строкой'
        assert value != '', 'Поле "Логин" пустое'
        assert 4 <= len(
            value) <= 15, 'Поле "Логин" должно занимать от 4 до 15 символов'
        assert not value.isnumeric(), 'Логин не может состоять только из чисел'

        self.__login = value

    @property
    def password(self):  # функция чтения из поля __password
        return self.__password

    @password.setter
    def password(self, value: str):
        assert type(value) == str, 'Пароль должен быть строкой'
        assert value != '', 'Поле "Пароль" пустое'
        assert 6 <= len(
            value) <= 15, 'Поле "Пароль" должно занимать от 6 до 15 символов'

        self.__password = value

    @property
    def age(self):  # функция чтения из поля __age
        return self.__age

    @age.setter
    def age(self, value: int):
        assert type(value) == int, 'Возраст должен быть числом'
        assert 0 < value <= 120, 'Возраст должен быть от 1 до 120'

        self.__age = value

    def __init__(self, settings: UserSettings) -> None:
        # 1 раз при создании объекта
        self.login = settings.login
        self.password = settings.password
        self.age = settings.age

    def print_user(self):
        print(self.__login, self.__password, self.__age)


user = UserConstructor(login='User1', password='12314142', age=18)


user_settings = UserSettings(login='User1', password='12314142', age=18)
user2 = UserObject(user_settings)


user_constructor_list1 = [
    UserConstructor(login='User1', password='12314142', age=18),
    UserConstructor(login='User2', password='4234234', age=20),
    UserConstructor(login='User3', password='1231412314142', age=11),
    UserConstructor(login='User4', password='35', age=18),
    UserConstructor(login='User5', password='12314345435142', age=15)]

user_settings = [
    UserSettings(login='User1', password='12314142', age=18),
    UserSettings(login='User2', password='4234234', age=20),
    UserSettings(login='User3', password='1231412314142', age=11),
    UserSettings(login='User4', password='35', age=18),
    UserSettings(login='User5', password='12314345435142', age=15)    
]

user_constructor_list2 = [
    UserObject(user_settings[0]),
    UserObject(user_settings[1]),
    UserObject(user_settings[2]),
    UserObject(user_settings[3]),
    UserObject(user_settings[4]),
]
