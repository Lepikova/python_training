
from model.contact import Contact

def test_update_contact(app):
    app.session.login("admin", "secret")
    app.contact.update_contact(Contact(firstname="Igor", middlename="Iva", lastname="Ivanov", nickname="Vano", title="First", address="Spb", company="Leno", homenomber="123", worknomber="12344", mobilenomber="32123", fax="321", email="1234@mail.ru", bday="20", bmonth="October", byear="1990"))
    app.session.logout()