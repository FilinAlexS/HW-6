from page_object.add_product_page import AddProductPage
from data.iphone_15 import Iphone15


def test_add_new_product_on_admin_page(browser):
    admin = AddProductPage(browser)
    admin.open(browser.url)
    admin.login_to_admin()
    admin.create_a_product()
    admin.save_change()
    assert admin.check_add_new_product(Iphone15.PRODUCT_NAME)


def test_deleting_new_product(browser):
    admin = AddProductPage(browser)
    admin.open(browser.url)
    admin.login_to_admin()
    admin.go_to_products_in_catalog()
    admin.delete_product_by_name(Iphone15.PRODUCT_NAME)
    assert admin.check_absence_new_product(Iphone15.PRODUCT_NAME)
