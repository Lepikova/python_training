from model.group import Group

def test_update_first_group(app):
    app.session.login("admin", "secret")
    app.group.update_first_group(Group(name="номер", header="обновления", footer="группы"))
    app.session.logout()