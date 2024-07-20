from model.group import Group

def test_delete_first_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="чтобы было", header="чтобы было", footer="чтобы было"))
    app.group.delete_first_group()
