
from model.contact import Contact

def test_update_contact_firstname(app):
    app.contact.update_contact(Contact(firstname="Huan"))

def test_update_contact_middlename(app):
    app.contact.update_contact(Contact(middlename="Paablo"))

def test_update_contact_lastname(app):
    app.contact.update_contact(Contact(lastname="Петрович"))
