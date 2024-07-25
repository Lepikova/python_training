
from model.contact import Contact

def test_update_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.creating(Contact(firstname="чтобы было", lastname="чтобы было"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Huan")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    app.contact.update_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_update_contact_lastname(app):
#    if app.contact.count_contacts() == 0:
#        app.contact.creating(Contact(firstname="чтобы было", lastname="чтобы было"))
#    old_contacts = app.contact.get_contact_list()
#   app.contact.update_contact(Contact(lastname="Paablo"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)

#def test_update_contact_mobilenomber(app):
#    if app.contact.count_contacts() == 0:
#        app.contact.creating(Contact(firstname="чтобы было", lastname="чтобы было", mobilenomber="0000000"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.update_contact(Contact(mobilenomber="123321"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
