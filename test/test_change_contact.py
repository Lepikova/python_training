
from model.contact import Contact

def test_update_contact_firstname(app):
    app.session.login("admin", "secret")
    app.contact.update_contact(Contact(firstname="Huan"))
    app.session.logout()

def test_update_contact_middlename(app):
    app.session.login("admin", "secret")
    app.contact.update_contact(Contact(middlename="Paablo"))
    app.session.logout()

def test_update_contact_lastname(app):
    app.session.login("admin", "secret")
    app.contact.update_contact(Contact(lastname="Петрович"))
    app.session.logout()