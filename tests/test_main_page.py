import pytest
from page_object.main_page import MainPage


def test_element_of_main_page(browser):
    main = MainPage(browser)
    main.open(browser.url)
    main.find_input_field_search()
    main.find_logo_img()
    main.find_button_cart()
    main.find_first_element_in_featured()
    main.find_second_button_add_to_cart_in_featured()


@pytest.mark.parametrize('currency', ['EUR', 'GBP', 'USD'])
def test_currency(browser, currency):
    main = MainPage(browser)
    main.open(browser.url)
    main.currency_selection(currency)
    main.check_currency_menu_and_cart(currency)
