from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.creating(Contact(firstname="чтобы было", middlename="чтобы было", mobilenomber="0000000"))
    app.contact.delete_first_contact()


