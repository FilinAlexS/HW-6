from page_object.admin_page import AdminPage


def test_find_elements_on_login_admin_page(browser):
    admin = AdminPage(browser)
    admin.open(browser.url)
    admin.find_input_field_username()
    admin.find_input_field_password()
    admin.find_button_login()
    admin.find_text_opencart_in_footer()
    admin.check_text_in_cardheader()


def test_login_admin_page(browser):
    login_admin = AdminPage(browser)
    login_admin.open(browser.url)
    login_admin.input_username("admin")
    login_admin.input_password("admin")
    login_admin.submit_login()
    assert login_admin.userpic_is_visible()
