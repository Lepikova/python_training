# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*4
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])

def random_phone_number():
    digits = string.digits
    return "7" + "".join([random.choice(digits) for _ in range(10)])

def random_month():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    return random.choice(months)

def random_day():
    return str(random.randint(1, 31))

def random_year():
    return str(random.randint(1900, 2024))

def random_email(prefix, maxlen):
    domains = ["gmail.com", "yahoo.com", "mail.ru", "yandex.ru", "outlook.com"]
    return (prefix + "".join([random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, maxlen))])
            + "@" + random.choice(domains))

testdata = [Contact(firstname=random_string("first", 10), middlename=random_string("middle", 10),
                    lastname=random_string("last", 10), nickname=random_string("nick", 10),
                    title=random_string("title", 10), address=random_string("address", 30),
                    company=random_string("comp", 10), homenomber=random_phone_number(),
                    worknomber=random_phone_number(), mobilenomber=random_phone_number(), fax=random_phone_number(),
                    email=random_email("email", 10), email2=random_email("email", 10),
                    email3=random_email("email", 10), bday=random_day(), bmonth=random_month(), byear=random_year())
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.creating(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



