from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

REGISTER_PAGE = '/index.php?route=account/register'


class RegisterPage:
    PATH = REGISTER_PAGE

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url + self.PATH)

    def find_input_field_firstname(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@name='firstname']")))

    def input_firstname(self, text):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@name='firstname']"))).click()
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@name='firstname']"))).clear()
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@name='firstname']"))).send_keys(text)

    def find_input_field_lastname(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@name='lastname']")))

    def input_lastname(self, text):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@name='lastname']"))).click()
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@name='lastname']"))).clear()
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@name='lastname']"))).send_keys(text)

    def find_input_field_password(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='input-password']")))

    def input_password(self, text):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='input-password']"))).click()
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='input-password']"))).clear()
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='input-password']"))).send_keys(text)

        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='input-confirm']"))).click()
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='input-confirm']"))).clear()
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='input-confirm']"))).send_keys(text)

    def find_input_field_email(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@name='email']")))

    def input_email(self, text):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@name='email']"))).click()
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@name='email']"))).clear()
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@name='email']"))).send_keys(text)

    def input_telephone(self, text):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@name='telephone']"))).click()
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@name='telephone']"))).clear()
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@name='telephone']"))).send_keys(text)

    def find_checkbox_agree_policy(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@name='agree']")))

    def on_checkbox_agree_policy(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@name='agree']"))).click()

    def find_button_continue(self):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@type, 'submit')]")))

    def click_submit(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@type, 'submit')]"))).click()

    def click_continue(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//*/a[.='Continue']"))).click()

    def check_user_login(self):
        a = self.driver.find_element(By.XPATH, "//*[@id='column-right']/*/a[.='Logout']").is_displayed()
        return a
