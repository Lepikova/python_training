
from model.contact import Contact

def test_update_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.creating(Contact(firstname="чтобы было", middlename="чтобы было", mobilenomber="0000000"))
    app.contact.update_contact(Contact(firstname="Huan"))

def test_update_contact_middlename(app):
    if app.contact.count_contacts() == 0:
        app.contact.creating(Contact(firstname="чтобы было", middlename="чтобы было", mobilenomber="0000000"))
    app.contact.update_contact(Contact(middlename="Paablo"))

def test_update_contact_lastname(app):
    if app.contact.count_contacts() == 0:
        app.contact.creating(Contact(firstname="чтобы было", middlename="чтобы было", mobilenomber="0000000"))
    app.contact.update_contact(Contact(lastname="Петрович"))
