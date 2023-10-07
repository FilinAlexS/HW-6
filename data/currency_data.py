from selenium.webdriver.common.by import By


class CurrencyData:
    EUR = (By.XPATH, "//span[contains(text(),'0 item(s) - 0.00€')]")
    EUR_ACTIVE = (By.XPATH, "//strong[contains(text(),'€')]")
    USD = (By.XPATH, "//span[contains(text(),'0 item(s) - $0.00')]")
    USD_ACTIVE = (By.XPATH, "//strong[contains(text(),'$')]")
    GBP = (By.XPATH, "//span[contains(text(),'0 item(s) - £0.00')]")
    GBP_ACTIVE = (By.XPATH, "//strong[contains(text(),'£')]")
