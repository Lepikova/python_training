
from model.contact import Contact

def test_update_contact(app):
    app.session.login("admin", "secret")
    app.contact.update_contact(Contact(firstname="Igor", middlename="Semen", lastname="Petrov", nickname="wqer", title="Second", address="Moscow", company="Magnit", homenomber="proton", worknomber="00000", mobilenomber="54345", fax="77777", email="1234@yandex.ru", bday="10", bmonth="November", byear="1987"))
    app.session.logout()