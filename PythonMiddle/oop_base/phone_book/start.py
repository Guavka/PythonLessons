from models.contact import Contact, Phone, PhoneSettings


if __name__ == '__main__':
    phone1 = Phone(PhoneSettings(name='Домашний', number='0714561122'))
    phone2 = Phone(PhoneSettings(name='Домашний2', number='0714561122'))
    
    contact = Contact()
    contact.add_number(phone1)
    contact.add_number(phone2)
    
    for number in contact.numbers:
        print(contact.numbers[number])
