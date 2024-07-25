
from model.contact import Contact

def test_update_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.creating(Contact(firstname="чтобы было", middlename="чтобы было", mobilenomber="0000000"))
    old_contacts = app.contact.get_contact_list()
    app.contact.update_contact(Contact(firstname="Huan"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_update_contact_middlename(app):
    if app.contact.count_contacts() == 0:
        app.contact.creating(Contact(firstname="чтобы было", middlename="чтобы было", mobilenomber="0000000"))
    old_contacts = app.contact.get_contact_list()
    app.contact.update_contact(Contact(middlename="Paablo"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_update_contact_lastname(app):
    if app.contact.count_contacts() == 0:
        app.contact.creating(Contact(firstname="чтобы было", middlename="чтобы было", mobilenomber="0000000"))
    old_contacts = app.contact.get_contact_list()
    app.contact.update_contact(Contact(lastname="Петрович"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
