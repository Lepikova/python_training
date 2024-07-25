
from model.contact import Contact
from random import randrange


def test_update_some_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.creating(Contact(firstname="чтобы было", lastname="фамилия"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Huan")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    app.contact.update_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



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
