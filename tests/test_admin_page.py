from page_object.admin_page import LoginAdminPage, AdminPage
from data.iphone_15 import Iphone15


def test_find_elements_on_admin_page(browser):
    admin = LoginAdminPage(browser)
    admin.open(browser.url)
    admin.find_input_field_username()
    admin.find_input_field_password()
    admin.find_button_login()
    admin.find_text_opencart_in_footer()
    admin.check_text_in_cardheader()


def test_login_admin_page(browser):
    login_admin = LoginAdminPage(browser)
    login_admin.open(browser.url)
    login_admin.input_username("admin")
    login_admin.input_password("admin")
    login_admin.submit_login()
    assert login_admin.userpic_is_visible()


def test_add_new_product_on_admin_page(browser):
    test_login_admin_page(browser)
    admin = AdminPage(browser)
    admin.go_to_products_in_catalog()
    admin.click_button_add_new_in_products()
    admin.input_product_name(Iphone15.PRODUCT_NAME)
    admin.input_description(Iphone15.DESCRIPTION)
    admin.input_meta_tag(Iphone15.META_TAG)
    admin.go_to_data_tab()
    admin.input_model(Iphone15.MODEL)
    admin.input_price(Iphone15.PRICE)
    admin.input_quantity(Iphone15.QUANTITY)
    admin.go_to_links_tab()
    admin.input_manufacturer(Iphone15.MANUFACTURER)
    admin.input_category(Iphone15.CATEGORY)
    admin.go_to_seo_tab()
    admin.input_seo(Iphone15.SEO)
    admin.go_to_image_tab()
    admin.change_default_image()
    admin.save_change()
    assert admin.check_add_new_product(Iphone15.PRODUCT_NAME)


def test_delete_new_product(browser):
    test_login_admin_page(browser)
    admin = AdminPage(browser)
    admin.go_to_products_in_catalog()
    admin.delete_product_by_name(Iphone15.PRODUCT_NAME)
    assert admin.check_absence_new_product(Iphone15.PRODUCT_NAME)

