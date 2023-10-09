from selenium.webdriver.common.by import By


class CatalogLocators:
    CATALOG_PAGE = '/index.php?route=product/category&path=20'
    FIELD_SORTBY = (By.XPATH, "//*[@id='input-sort']")
    ICON_HOME = (By.XPATH, "//*[contains(@class, 'fa-home')]")
    BUTTON_LIST_VIEW = (By.XPATH, "//*[@id='list-view']")
    BUTTON_COMPAREADD = (By.XPATH, "//*/button[contains(@onclick, 'compare.add')]")
    CAMERAS_IN_LEFT_MENU = (By.XPATH, "//*[@id='column-left']//a[9]")
