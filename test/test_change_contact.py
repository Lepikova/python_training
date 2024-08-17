
from model.contact import Contact
import random

def test_update_some_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.creating(Contact(firstname="чтобы было", lastname="фамилия"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    update_contact = Contact(firstname="Huan")
    update_contact.id = contact.id
    update_contact.lastname = contact.lastname
    app.contact.update_contact_by_id(contact.id, update_contact)
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(update_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



#def test_update_contact_lastname(app):
#    if app.contact.count_contacts() == 0:
#        app.contact.creating(Contact(firstname="чтобы было", lastname="фамилия"))
#    old_contacts = app.contact.get_contact_list()
#   app.contact.update_contact(Contact(lastname="Paablo"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)

#def test_update_contact_mobilenomber(app):
#    if app.contact.count_contacts() == 0:
#        app.contact.creating(Contact(firstname="чтобы было", lastname="фамилия", mobilenomber="0000000"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.update_contact(Contact(mobilenomber="123321"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
