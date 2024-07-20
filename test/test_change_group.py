from model.group import Group

def test_update_first_group_name(app):
    app.group.update_first_group(Group(name="uno"))

def test_update_first_group_header(app):
    app.group.update_first_group(Group(header="dos"))

def test_update_first_group_footer(app):
    app.group.update_first_group(Group(footer="tres"))
