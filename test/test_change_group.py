from model.group import Group

def test_update_first_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="чтобы было", header="чтобы было", footer="чтобы было"))
    old_groups = app.group.get_group_list()
    app.group.update_first_group(Group(name="uno"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_update_first_group_header(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="чтобы было", header="чтобы было", footer="чтобы было"))
    old_groups = app.group.get_group_list()
    app.group.update_first_group(Group(header="dos"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_update_first_group_footer(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="чтобы было", header="чтобы было", footer="чтобы было"))
    old_groups = app.group.get_group_list()
    app.group.update_first_group(Group(footer="tres"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
