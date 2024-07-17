from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def creating(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.open_creating_contact()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.app.return_to_home_page()

    def fill_contact_form(self, contact):
        self.filling_contact_write("firstname", contact.firstname)
        self.filling_contact_write("middlename", contact.middlename)
        self.filling_contact_write("lastname", contact.lastname)
        self.filling_contact_write("nickname", contact.nickname)
        self.filling_contact_write("title", contact.title)
        self.filling_contact_write("address", contact.address)
        self.filling_contact_write("company", contact.company)
        self.filling_contact_write("home", contact.homenomber)
        self.filling_contact_write("work", contact.worknomber)
        self.filling_contact_write("mobile", contact.mobilenomber)
        self.filling_contact_write("fax", contact.fax)
        self.filling_contact_write("email", contact.email)
        self.filling_contact_choose("bday", contact.bday)
        self.filling_contact_choose("bmonth", contact.bmonth)
        self.filling_contact_write("byear", contact.byear)

    def filling_contact_choose(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def filling_contact_write(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_creating_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.app.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()

    def update_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
