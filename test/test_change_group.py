from model.group import Group
from random import randrange

def test_update_some_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="чтобы было", header="чтобы было", footer="чтобы было"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="uno")
    group.id = old_groups[index].id
    app.group.update_group_by_index(index, group)
    assert len(old_groups) == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



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
