from page_object.base_page import BasePage
from page_object.elements.register_locators import RegisterLocators


class RegisterPage(BasePage):
    PATH = RegisterLocators.REGISTER_PAGE

    def open(self, url):
        self.driver.get(url + self.PATH)

    def find_input_field_firstname(self):
        self.element(RegisterLocators.FIRSTNAME)

    def input_firstname(self, text):
        self._input(self.element(RegisterLocators.FIRSTNAME), text)

    def find_input_field_lastname(self):
        self.element(RegisterLocators.LASTNAME)

    def input_lastname(self, text):
        self._input(self.element(RegisterLocators.LASTNAME), text)

    def find_input_field_password(self):
        self.element(RegisterLocators.PASSWORD)

    def input_password(self, text):
        self._input(self.element(RegisterLocators.PASSWORD), text)
        self._input(self.element(RegisterLocators.CONFIRM_PASSWORD), text)

    def find_input_field_email(self):
        self.element(RegisterLocators.PASSWORD)

    def input_email(self, text):
        self._input(self.element(RegisterLocators.EMAIL), text)

    def input_telephone(self, text):
        self._input(self.element(RegisterLocators.TELEPHONE), text)

    def find_checkbox_agree_policy(self):
        self.element(RegisterLocators.CHECKBOX_AGREE_POLICY)

    def on_checkbox_agree_policy(self):
        self.click(self.element(RegisterLocators.CHECKBOX_AGREE_POLICY))

    def find_button_submit(self):
        self.element(RegisterLocators.SUBMIT)

    def click_submit(self):
        self.click(self.element(RegisterLocators.SUBMIT))

    def click_continue(self):
        self.click(self.element(RegisterLocators.BUTTON_CONTINUE))

    def check_user_login(self):
        return self.is_visible_element(RegisterLocators.LOGOUT)
