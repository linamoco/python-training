

class SessionHelper:

    def __init__(self, app):
        self.app = app
    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        # добавила поиск по данным со стартовой страницы
        # так как драйвер не успевает разлогиниться, а где и как поставить wait я не поняла
        wd.find_element_by_name("user")
        wd.find_element_by_name("pass")

