from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
from page_object.elements.main_locators import MainLocators


class MainPage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def find_input_field_search(self):
        self.element(MainLocators.FIELD_SEARCH)

    def find_logo_img(self):
        self.element(MainLocators.LOGO_IMG)

    def find_button_cart(self):
        self.element(MainLocators.BUTTON_CART)

    def find_first_element_in_featured(self):
        list_featured = self.elements(MainLocators.ALL_ELEMENTS_IN_FEATURED)
        return list_featured[0]

    def find_second_button_add_to_cart_in_featured(self):
        return self.elements(MainLocators.ALL_BUTTONS_ADD_TO_CART_IN_FEATURED)[1]

    def currency_selection(self, text):
        self.click(self.element(MainLocators.CURRENCY_BUTTON))
        self.click(self.element((By.NAME, f"{text}")))

    def check_currency_menu_and_cart(self, currency):
        self.element(MainLocators.currency_mapper.get(currency).get("active_currency_list"))
        self.element(MainLocators.currency_mapper.get(currency).get("currency_in_cart"))
