from model.group import Group

def test_update_first_group_name(app):
    app.session.login("admin", "secret")
    app.group.update_first_group(Group(name="uno"))
    app.session.logout()

def test_update_first_group_header(app):
    app.session.login("admin", "secret")
    app.group.update_first_group(Group(header="dos"))
    app.session.logout()

def test_update_first_group_footer(app):
    app.session.login("admin", "secret")
    app.group.update_first_group(Group(footer="tres"))
    app.session.logout()