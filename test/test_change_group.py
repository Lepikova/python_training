from model.group import Group
from random import randrange
import random

def test_update_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="чтобы было", header="чтобы было", footer="чтобы было"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    updated_group = Group(name="uno")
    updated_group.id = group.id
    app.group.update_group_by_id(group.id, updated_group)
    assert len(old_groups) == app.group.count_groups()
    new_groups=db.get_group_list()
    old_groups.remove(group)
    old_groups.append(updated_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_update_first_group_header(app):
#    if app.group.count_groups() == 0:
#        app.group.create(Group(name="чтобы было", header="чтобы было", footer="чтобы было"))
#    old_groups = app.group.get_group_list()
#    app.group.update_first_group(Group(header="dos"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_update_first_group_footer(app):
#    if app.group.count_groups() == 0:
#        app.group.create(Group(name="чтобы было", header="чтобы было", footer="чтобы было"))
#    old_groups = app.group.get_group_list()
#    app.group.update_first_group(Group(footer="tres"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
