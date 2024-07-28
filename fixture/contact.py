from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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
        self.contact_cache = None


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
        self.filling_contact_write("email2", contact.email2)
        self.filling_contact_write("email3", contact.email3)
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
       self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.app.return_to_home_page()
        self.contact_cache = None


    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_name("selected[]")[index].click()


    def update_first_contact(self, contact):
        self.update_contact_by_index(0, contact)

    def update_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.open_edit_page_by_index(index)
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def open_edit_page_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        rows = wd.find_elements_by_name("entry")
        if index < len(rows):
            row = rows[index]
            # Найти и нажать кнопку Edit
            edit_button = row.find_element_by_css_selector("a[href*='edit.php?id=']")
            edit_button.click()

    def open_view_page_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        rows = wd.find_elements_by_name("entry")
        if index < len(rows):
            row = rows[index]
            # Найти и нажать кнопку Details
            details_button = row.find_element_by_css_selector("a[href*='view.php?id=']")
            details_button.click()

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def count_contacts(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            # Поиск всех строк таблицы с контактами
            rows = wd.find_elements_by_css_selector("tr[name='entry']")
            for row in rows:
                cells = row.find_elements_by_tag_name("td")
                # Получаем ID контакта из чекбокса
                checkbox = cells[0].find_element_by_tag_name("input")
                id = checkbox.get_attribute("value")
                # Имя и фамилия находятся в других ячейках
                lastname = cells[1].text
                firstname = cells[2].text
                # Адрес
                address = cells[3].text
                # Вычленяем телефоны
                all_phones = cells[5].text
                # Вычленяем emails
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_page_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        homenomber = wd.find_element_by_name('home').get_attribute('value')
        worknomber = wd.find_element_by_name('work').get_attribute('value')
        mobilenomber = wd.find_element_by_name('mobile').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')

        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homenomber=homenomber, mobilenomber=mobilenomber,
                       worknomber=worknomber, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        homenomber = re.search("H: (.*)", text).group(1)
        mobilenomber = re.search("M: (.*)", text).group(1)
        worknomber = re.search("W: (.*)", text).group(1)
        return Contact(homenomber=homenomber, mobilenomber=mobilenomber,
                       worknomber=worknomber)










