from page_object.register_page import RegisterPage
from data.fake_user import fake_name, fake_last_name, fake_email, fake_phone, fake_password


def test_element_register_page(browser):
    register = RegisterPage(browser)
    register.open(browser.url)
    register.find_input_field_firstname()
    register.find_input_field_lastname()
    register.find_input_field_email()
    register.find_input_field_password()
    register.find_checkbox_agree_policy()
    register.find_button_submit()


def test_register_user(browser):
    register = RegisterPage(browser)
    register.open(browser.url)
    register.input_firstname(fake_name())
    register.input_lastname(fake_last_name())
    register.input_email(fake_email())
    register.input_telephone(fake_phone())
    register.input_password(fake_password())
    register.on_checkbox_agree_policy()
    register.click_submit()
    register.click_continue()
    assert register.check_user_login()
