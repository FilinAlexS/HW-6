from page_object.base_page import BasePage
from page_object.elements.catalog_locators import CatalogLocators


class CatalogPage(BasePage):
    PATH = CatalogLocators.CATALOG_PAGE

    def open(self, url):
        self.driver.get(url + self.PATH)

    def find_field_sortby(self):
        self.element(CatalogLocators.FIELD_SORTBY)

    def find_icon_home(self):
        self.element(CatalogLocators.ICON_HOME)

    def find_button_list_view(self):
        self.element(CatalogLocators.BUTTON_LIST_VIEW)

    def find_last_button_compareadd(self):
        return self.elements(CatalogLocators.BUTTON_COMPAREADD)[-1]

    def check_category_cameras_in_left_menu(self):
        self.verify_text_in_element(CatalogLocators.CAMERAS_IN_LEFT_MENU, "Cameras")
