from dataclasses import dataclass


@dataclass
class User:
    name: str
    money: int

    def __str__(self):
        return f'Name: {self.name}\nMoney: {self.money}'


@dataclass
class Admin(User):
    priority: int
