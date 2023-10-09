from page_object.base_page import BasePage
from page_object.elements.product_locators import ProductLocators


class ProductPage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def go_to_product_card(self):
        self.click(self.element(ProductLocators.PRODUCT_CARD))

    def find_button_add_to_card(self):
        self.element(ProductLocators.BUTTON_ADD_TO_CARD)

    def find_rating(self):
        self.element(ProductLocators.RATING)

    def find_name_product(self):
        self.element(ProductLocators.NAME_PRODUCT)

    def find_button_compare(self):
        self.element(ProductLocators.BUTTON_COMPARE)

    def find_link_specification(self):
        self.element(ProductLocators.LINK_SPECIFICATION)
