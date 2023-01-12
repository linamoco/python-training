# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def fill_field(self, name_element, text):
        wd = self.wd
        wd.find_element_by_name(name_element).click()
        wd.find_element_by_name(name_element).clear()
        wd.find_element_by_name(name_element).send_keys(text)

    def create_user(self, contact):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_field("firstname", contact.first_name)
        self.fill_field("middlename", contact.middle_name)
        self.fill_field("lastname", contact.last_name)
        self.fill_field("nickname", contact.nickname)
        self.fill_field("title", contact.title)
        self.fill_field("company", contact.company)
        self.fill_field("address", contact.address)
        self.fill_field("home", contact.home)
        self.fill_field("mobile", contact.mobile)
        self.fill_field("work", contact.work)
        self.fill_field("fax", contact.fax)
        self.fill_field("email", contact.email)
        self.fill_field("email2", contact.email2)
        self.fill_field("email3", contact.email3)
        self.fill_field("homepage", contact.homepage)

        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthday_day)
        wd.find_element_by_xpath(f"//option[@value='{contact.birthday_day}']").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthday_month)
        self.fill_field("byear", contact.birthday_year)

        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        self.fill_field("ayear", contact.anniversary_year)

        self.fill_field("address2", contact.secondary_address)
        self.fill_field("phone2", contact.secondary_home)
        self.fill_field("notes", contact.secondary_notes)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()