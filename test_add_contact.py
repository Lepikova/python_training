# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_contact import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(app):
    app.login("admin", "secret")
    app.creating_contact(Contact(firstname="Ivan", middlename="Iva", lastname="Ivanov", nickname="Vano", title="First", address="Spb", company="Leno", homenomber="123", worknomber="12344", mobilenomber="32123", fax="321", email="1234@mail.ru", bday="20", bmonth="October", byear="1990"))
    app.logout()