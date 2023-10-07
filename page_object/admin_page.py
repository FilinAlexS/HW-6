from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ADMIN_PAGE = '/admin'
TEXT_IN_CARD_HEADER = "Please enter your login details."


class LoginAdminPage:
    PATH = ADMIN_PAGE

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url + self.PATH)

    def find_input_field_username(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@name='username']")))

    def find_input_field_password(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='input-password']")))

    def find_text_opencart_in_footer(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='OpenCart']")))

    def find_button_login(self):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@type, 'submit')]")))

    def check_text_in_cardheader(self):
        WebDriverWait(self.driver, 3).until(
            EC.text_to_be_present_in_element((By.XPATH, '//h1'), TEXT_IN_CARD_HEADER))

    def input_username(self, text):
        self.driver.find_element(By.ID, "input-username").click()
        self.driver.find_element(By.ID, "input-username").clear()
        self.driver.find_element(By.ID, "input-username").send_keys(text)

    def input_password(self, text):
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys(text)

    def submit_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    def userpic_is_visible(self):
        visible = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, '//img[contains(@title, "admin")]'))).is_displayed()
        return visible


class AdminPage:
    PATH = ADMIN_PAGE

    def __init__(self, driver):
        self.driver = driver

    def go_to_products_in_catalog(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="menu-catalog"]'))).click()
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//a[.="Products"]'))).click()

    def click_button_add_new_in_products(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="pull-right"]/a'))).click()

    def input_product_name(self, text):
        self.driver.find_element(By.ID, "input-name1").click()
        self.driver.find_element(By.ID, "input-name1").clear()
        self.driver.find_element(By.ID, "input-name1").send_keys(text)

    def input_description(self, text):
        self.driver.find_element(By.XPATH, '//*[@class="note-editable"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="note-editable"]').clear()
        self.driver.find_element(By.XPATH, '//*[@class="note-editable"]').send_keys(text)

    def input_meta_tag(self, text):
        self.driver.find_element(By.ID, "input-meta-title1").click()
        self.driver.find_element(By.ID, "input-meta-title1").clear()
        self.driver.find_element(By.ID, "input-meta-title1").send_keys(text)

    def go_to_data_tab(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//a[.="Data"]'))).click()

    def input_model(self, text):
        self.driver.find_element(By.ID, "input-model").click()
        self.driver.find_element(By.ID, "input-model").clear()
        self.driver.find_element(By.ID, "input-model").send_keys(text)

    def input_price(self, text):
        self.driver.find_element(By.ID, "input-price").click()
        self.driver.find_element(By.ID, "input-price").clear()
        self.driver.find_element(By.ID, "input-price").send_keys(text)

    def input_quantity(self, text):
        self.driver.find_element(By.ID, "input-quantity").click()
        self.driver.find_element(By.ID, "input-quantity").clear()
        self.driver.find_element(By.ID, "input-quantity").send_keys(text)

    def go_to_links_tab(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//a[.="Links"]'))).click()

    def input_manufacturer(self, text):
        self.driver.find_element(By.ID, "input-manufacturer").click()
        self.driver.find_element(By.ID, "input-manufacturer").clear()
        self.driver.find_element(By.ID, "input-manufacturer").send_keys(text)
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, f'//a[.="{text}"]'))).click()

    def input_category(self, text):
        self.driver.find_element(By.ID, "input-category").click()
        self.driver.find_element(By.ID, "input-category").clear()
        self.driver.find_element(By.ID, "input-category").send_keys(text)
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, f'//a[.="{text}"]'))).click()

    def go_to_seo_tab(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//a[.="SEO"]'))).click()

    def input_seo(self, text):
        self.driver.find_element(By.NAME, "product_seo_url[0][1]").click()
        self.driver.find_element(By.NAME, "product_seo_url[0][1]").clear()
        self.driver.find_element(By.NAME, "product_seo_url[0][1]").send_keys(text)

    def go_to_image_tab(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//a[.="Image"]'))).click()

    def change_default_image(self):
        self.driver.find_element(By.ID, "thumb-image").click()
        a = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, "button-image")))
        time.sleep(1)
        a.click()
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='directory']"))).click()

        time.sleep(1)
        b = WebDriverWait(self.driver, 2).until(
            EC.visibility_of_any_elements_located((By.XPATH, "//*[@class='directory']")))
        b[2].click()

        time.sleep(1)
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//img[contains(@alt,'iphone.jpg')]"))).click()

    def save_change(self):
        self.driver.find_element(By.XPATH, "//button[contains(@type, 'submit')]").click()

    def find_product_by_name(self, text):
        a = WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[@class='text-left'][.='{text}']")))
        return a

    def check_add_new_product(self, text):
        item = self.find_product_by_name(text).is_displayed()
        return item

    def _click_button_delete(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="btn btn-danger"]'))).click()

    def delete_product_by_name(self, text):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(
            (By.XPATH, f"//td[@class='text-left' and text()='{text}']/preceding-sibling::td/input"))).click()
        self._click_button_delete()
        self.driver.switch_to.alert.accept()

    def check_absence_new_product(self, text):
        item = self.driver.find_elements(By.XPATH,
                                         f"//td[@class='text-left' and text()='{text}']/preceding-sibling::td/input")
        a = []
        return 1 if item == a else 0
