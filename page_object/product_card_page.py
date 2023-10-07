from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        self.driver.find_element(By.XPATH, '//*[contains(@class, "image")]/a/img').click()

    def find_button_add_to_card(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="button-cart"]')))

    def find_rating(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(@class, "rating")]')))

    def find_name_product(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*/h1')))

    def find_button_compare(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//*/button[contains(@onclick, "compare.add")]')))

    def find_link_specification(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//a[.="Specification"]')))
