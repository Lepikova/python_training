from model.group import Group
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        # return to groups page
        wd.find_element_by_link_text("group page").click()

    def create(self, party):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(party)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.filling("group_name", group.name)
        self.filling("group_header", group.header)
        self.filling("group_footer", group.footer)


    def filling(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def update_first_group(self, upd):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.filling("group_name", upd.name)
        self.filling("group_header", upd.header)
        self.filling("group_footer", upd.footer)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def count_groups(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_group_page()
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups





