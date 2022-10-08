from typing import Dict

from models.contact import Contact


class PhoneBook:
    """
    Класс, который содержит в себе все контакты
    """
    __contacts: Dict[str, Contact] = {}

    @property
    def contacts(self):
        from copy import deepcopy
        return deepcopy(self.__contacts)

    def add_contact(self, contact: Contact):
        assert isinstance(contact, Contact), 'Неверный контакт'

        assert not (
            contact.first_name in self.__contacts), 'Данный контакт уже существует'

        self.__contacts[contact.first_name] = contact
