import re

def test_all_contacts_on_home_page(app, db):
    contacts_from_db = db.get_contact_list()
    contacts_from_home_page = app.contact.get_contact_list()
    assert len(contacts_from_home_page) == len(contacts_from_db)
    for contact_from_home_page in contacts_from_home_page:
        contact_from_db = next(filter(lambda x: x.id == contact_from_home_page.id, contacts_from_db))
        assert contact_from_home_page.firstname == contact_from_db.firstname.strip()
        assert contact_from_home_page.lastname == contact_from_db.lastname.strip()
        assert contact_from_home_page.address == contact_from_db.address.strip()
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)



#def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_view_page.homenomber == contact_from_edit_page.homenomber
#    assert contact_from_view_page.worknomber == contact_from_edit_page.worknomber
#    assert contact_from_view_page.mobilenomber == contact_from_edit_page.mobilenomber

def clear(phone):
    return re.sub("[() -]", "", phone) if phone else ""

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), [contact.homenomber, contact.mobilenomber, contact.worknomber])))

def clear_email(email):
    return email.strip() if email else ""

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_email(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
