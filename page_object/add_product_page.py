from selenium.webdriver.common.by import By
from data.iphone_15 import Iphone15
from page_object.admin_page import AdminPage
from page_object.elements.product_locators import AddProductLocators
import time


class AddProductPage(AdminPage):

    def go_to_products_in_catalog(self):
        self.click(self.element(AddProductLocators.MENU_CATALOG))
        self.click(self.element(AddProductLocators.MENU_PRODUCT))

    def click_button_add_new_in_products(self):
        self.click(self.element(AddProductLocators.ADD_NEW))

    def input_product_name(self, text):
        self._input(self.element(AddProductLocators.PRODUCT_NAME), text)

    def input_description(self, text):
        self._input(self.element(AddProductLocators.DESCRIPTION), text)

    def input_meta_tag(self, text):
        self._input(self.element(AddProductLocators.META_TAG), text)

    def go_to_data_tab(self):
        self.click(self.element(AddProductLocators.DATA_TAB))

    def input_model(self, text):
        self._input(self.element(AddProductLocators.MODEL), text)

    def input_price(self, text):
        self._input(self.element(AddProductLocators.PRICE), text)

    def input_quantity(self, text):
        self._input(self.element(AddProductLocators.QUANTITY), text)

    def go_to_links_tab(self):
        self.click(self.element(AddProductLocators.LINKS_TAB))

    def input_manufacturer(self, text):
        self._input(self.element(AddProductLocators.MANUFACTURER), text)
        self.click(self.element((By.XPATH, f'//a[.="{text}"]')))

    def input_category(self, text):
        self._input(self.element(AddProductLocators.CATEGORY), text)
        self.click(self.element((By.XPATH, f'//a[.="{text}"]')))

    def go_to_seo_tab(self):
        self.click(self.element(AddProductLocators.SEO_TAB))

    def input_seo(self, text):
        self._input(self.element(AddProductLocators.SEO), text)

    def go_to_image_tab(self):
        self.click(self.element(AddProductLocators.IMAGE_TAB))

    def change_default_image(self):
        self.click(self.element(AddProductLocators.IMAGE))
        self.click(self.element(AddProductLocators.BUTTON_EDIT_IMAGE))
        self.click(self.element(AddProductLocators.DIRECTORY))
        time.sleep(0.2)
        self.click(self.elements(AddProductLocators.DIRECTORY)[2])
        self.click(self.element(AddProductLocators.IMAGE_IPHONE))

    def save_change(self):
        self.click(self.element(AddProductLocators.SAVE))

    def _find_product_by_name(self, text):
        return self.element((By.XPATH, f"//*[@class='text-left'][.='{text}']"))

    def check_add_new_product(self, text):
        return self._find_product_by_name(text).is_displayed()

    def _click_button_delete(self):
        self.click(self.element(AddProductLocators.BUTTON_DELETE))

    def delete_product_by_name(self, text):
        self.click(
            self.element((By.XPATH, f"//td[@class='text-left' and text()='{text}']/preceding-sibling::td/input")))
        self._click_button_delete()
        self.driver.switch_to.alert.accept()

    def check_absence_new_product(self, text):
        item = self.driver.find_elements(By.XPATH,
                                         f"//td[@class='text-left' and text()='{text}']/preceding-sibling::td/input")
        a = []
        return 1 if item == a else 0

    def create_a_product(self):
        self.go_to_products_in_catalog()
        self.click_button_add_new_in_products()
        self.input_product_name(Iphone15.PRODUCT_NAME)
        self.input_description(Iphone15.DESCRIPTION)
        self.input_meta_tag(Iphone15.META_TAG)
        self.go_to_data_tab()
        self.input_model(Iphone15.MODEL)
        self.input_price(Iphone15.PRICE)
        self.input_quantity(Iphone15.QUANTITY)
        self.go_to_links_tab()
        self.input_manufacturer(Iphone15.MANUFACTURER)
        self.input_category(Iphone15.CATEGORY)
        self.go_to_seo_tab()
        self.input_seo(Iphone15.SEO)
        self.go_to_image_tab()
        self.change_default_image()
