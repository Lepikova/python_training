import random
import time
from model.group import Group
from model.contact import Contact

def test_remove_contact_from_group(app, orm):
    # Получаю все группы с контактами
    groups_with_contacts = [group for group in orm.get_group_list() if orm.get_contacts_in_group(group)]
    # Если нет групп с контактами, добавляю случайный контакт в случайную группу
    if not groups_with_contacts:
        # Проверяю наличие групп, если нет, создаю группу
        if len(orm.get_group_list()) == 0:
            app.group.create(Group(name="чтобы было", header="чтобы было", footer="чтобы было"))
        # Получаю контакты, которые не в группе, если их нет — создаю контакт
        contacts_not_in_groups = orm.get_contacts_not_in_any_group()
        if not contacts_not_in_groups:
            app.contact.creating(Contact(firstname="чтобы было", lastname="фамилия", mobilenomber="0000000"))
            contacts_not_in_groups = orm.get_contacts_not_in_any_group()
        assert contacts_not_in_groups
        random_contact = random.choice(contacts_not_in_groups)
        random_contact_id = random_contact.id
        # Выбираю случайную группу
        random_group = random.choice(orm.get_group_list())
        random_group_id = random_group.id
        # Добавляю контакт в группу
        app.contact.open_contacts_without_groups()
        app.contact.add_contact_to_group(random_contact_id, random_group_id)
        # Проверяю, что контакт добавлен в группу
        contacts_in_group = orm.get_contacts_in_group(random_group)
        assert any(c.id == random_contact_id for c in contacts_in_group)
        # Обновляю список групп с контактами после добавления
        groups_with_contacts = [group for group in orm.get_group_list() if orm.get_contacts_in_group(group)]
    # Проверяю, что группы с контактами есть после добавления
    assert groups_with_contacts
    # Выбираю случайную группу с контактами
    random_group = random.choice(groups_with_contacts)
    # Получаю все контакты в выбранной группе
    contacts_in_group = orm.get_contacts_in_group(random_group)
    # Проверяю, что в выбранной группе есть контакты
    assert contacts_in_group
    # Выбираю случайный контакт для удаления
    random_contact = random.choice(contacts_in_group)
    random_contact_id = random_contact.id
    # Удаляю контакт из группы через UI
    app.contact.remove_from_group(random_contact_id, random_group.id)
    # Добавляю повторную проверку с ожиданием, чтобы убедиться, что контакт удален (без этой проверки тест падает)
    def contact_is_removed():
        contacts_not_in_group = orm.get_contacts_not_in_group(random_group)
        return any(c.id == random_contact_id for c in contacts_not_in_group)
    for _ in range(5):
        if contact_is_removed():
            break
        time.sleep(2)
    else:
        assert False


