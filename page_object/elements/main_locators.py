from selenium.webdriver.common.by import By
from data.currency_data import CurrencyData


class MainLocators:
    FIELD_SEARCH = (By.XPATH, "//*[contains(@name, 'search')]")
    LOGO_IMG = (By.XPATH, "//*[@id='logo']//img")
    BUTTON_CART = (By.XPATH, "//*[@id='cart']/button")
    ALL_ELEMENTS_IN_FEATURED = (By.XPATH, "//h4/a")
    ALL_BUTTONS_ADD_TO_CART_IN_FEATURED = (By.XPATH, "//button[contains(@onclick, 'cart.add')]")
    CURRENCY_BUTTON = (By.XPATH, "//*[.='Currency']/..")

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
