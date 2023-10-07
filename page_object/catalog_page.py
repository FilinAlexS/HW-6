from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CATALOG_PAGE = '/index.php?route=product/category&path=20'


class CatalogPage:
    PATH = CATALOG_PAGE

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url + self.PATH)

    def find_field_sortby(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='input-sort']")))

    def find_icon_home(self):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'fa-home')]")))

    def find_button_list_view(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='list-view']")))

    def find_last_button_compareadd(self):
        list_button_compareadd = WebDriverWait(self.driver, 1).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*/button[contains(@onclick, 'compare.add')]")))
        return list_button_compareadd[-1]

    def check_category_cameras_in_left_menu(self):
        WebDriverWait(self.driver, 1).until(
            EC.text_to_be_present_in_element((By.XPATH, "//*[@id='column-left']//a[9]"), text_="Cameras"))
