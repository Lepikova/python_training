# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Iva", lastname="Ivanov", nickname="Vano",
                      title="First", address="Санкт-Петербург, Ленинский, 22-4", company="Leno", homenomber="123", worknomber="12344",
                      mobilenomber="32123", fax="321", email="1234@mail.ru", email2="1234@ya.ru",
                      email3="1234@ou.ru", bday="20", bmonth="October", byear="1990")
    app.contact.creating(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



