import random
from model.group import Group
from model.contact import Contact
import pytest

def test_add_random_contact_to_random_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="чтобы было", header="чтобы было", footer="чтобы было"))
    contacts_not_in_groups = orm.get_contacts_not_in_any_group()
    if not contacts_not_in_groups:
        app.contact.creating(Contact(firstname="чтобы было", lastname="фамилия", mobilenomber="0000000"))
        contacts_not_in_groups = orm.get_contacts_not_in_any_group()
    assert contacts_not_in_groups
    random_contact = random.choice(contacts_not_in_groups)
    random_contact_id = random_contact.id
    random_group = random.choice(orm.get_group_list())
    random_group_id = random_group.id
    app.contact.open_contacts_without_groups()
    app.contact.add_contact_to_group(random_contact_id, random_group_id)
    contacts_in_group = orm.get_contacts_in_group(random_group)
    assert any(c.id == random_contact_id for c in contacts_in_group)
