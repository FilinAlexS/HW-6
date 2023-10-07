from page_object.product_card_page import ProductPage


def test_find_element_on_product_card(browser):
    product_card = ProductPage(browser)
    product_card.open(browser.url)
    product_card.find_button_add_to_card()
    product_card.find_name_product()
    product_card.find_rating()
    product_card.find_button_compare()
    product_card.find_link_specification()
