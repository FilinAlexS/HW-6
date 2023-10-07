from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.currency_data import CurrencyData
from selenium.common.exceptions import TimeoutException


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_input_field_search(self):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@name, 'search')]")))

    def find_logo_img(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='logo']//img")))

    def find_button_cart(self):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='cart']/button")))

    def find_first_element_in_featured(self):
        list_featured = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//h4/a")))
        return list_featured[0]

    def find_button_add_to_cart(self):
        list_add_to_cart = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//button[contains(@onclick, 'cart.add')]")))
        return list_add_to_cart[0]

    def _click_currency_button(self):
        self.driver.find_element(By.XPATH, "//*[.='Currency']/..").click()

    def currency_selection(self, text):
        self._click_currency_button()
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.NAME, f"{text}"))).click()

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find elements by locator: {}".format(locator))

    def check_currency_menu_and_cart(self, currency):
        currency_mapper = {
            "EUR": {
                "active_currency_list": CurrencyData.EUR_ACTIVE,
                "currency_in_cart": CurrencyData.EUR
            },
            "USD": {
                "active_currency_list": CurrencyData.USD_ACTIVE,
                "currency_in_cart": CurrencyData.USD
            },
            "GBP": {
                "active_currency_list": CurrencyData.GBP_ACTIVE,
                "currency_in_cart": CurrencyData.GBP
            }
        }
        self._verify_element_presence(currency_mapper.get(currency).get("active_currency_list"))
        self._verify_element_presence(currency_mapper.get(currency).get("currency_in_cart"))
