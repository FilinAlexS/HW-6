from page_object.base_page import BasePage
from page_object.elements.admin_locators import AdminLocators


class AdminPage(BasePage):
    PATH = AdminLocators.ADMIN_PAGE

    def open(self, url):
        self.driver.get(url + self.PATH)

    def find_input_field_username(self):
        self.element(AdminLocators.FIELD_USERNAME)

    def find_input_field_password(self):
        self.element(AdminLocators.FIELD_PASSWORD)

    def find_text_opencart_in_footer(self):
        self.element(AdminLocators.TEXT_OPENCART_IN_FOOTER)

    def find_button_login(self):
        self.element(AdminLocators.BUTTON_LOGIN)

    def check_text_in_cardheader(self):
        self.verify_text_in_element(AdminLocators.TEXT_IN_CARDHEADER, AdminLocators.TEXT_IN_CARD_HEADER)

    def input_username(self, text):
        self._input(self.element(AdminLocators.FIELD_USERNAME), text)

    def input_password(self, text):
        self._input(self.element(AdminLocators.FIELD_PASSWORD), text)

    def submit_login(self):
        self.click(self.element(AdminLocators.BUTTON_LOGIN))

    def userpic_is_visible(self):
        return self.is_visible_element(AdminLocators.USERPIC)

    def login_to_admin(self):
        self.input_username('admin')
        self.input_password('admin')
        self.submit_login()
