import re

def tests_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert clear_phone(contact_from_home_page.homenomber) == clear_phone(contact_from_edit_page.homenomber)
    assert clear_phone(contact_from_home_page.worknomber) == clear_phone(contact_from_edit_page.worknomber)
    assert clear_phone(contact_from_home_page.mobilenomber) == clear_phone(contact_from_edit_page.mobilenomber)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homenomber == contact_from_edit_page.homenomber
    assert contact_from_view_page.worknomber == contact_from_edit_page.worknomber
    assert contact_from_view_page.mobilenomber == contact_from_edit_page.mobilenomber

def clear_phone(phone):
    re.sub("[^0-9]", "", phone)