from pages.page_home import HomePage
from tests.test_login import test_standard_user

def test_check_add_product_to_shopping_cart(page):
    start = HomePage(page)

    test_standard_user(page)
    start.click_product_select("Sauce Labs Fleece Jacket")
    start.product_price_check("49.99")
    start.click_add_to_cart()
    start.cart_amount_check("1")
    start.click_back_to_products()
    start.check_swag_logo_is_visible()

def test_check_sorting_low_high(page):
    start = HomePage(page)

    test_standard_user(page)
    start.click_sorting_dropdown()
    start.click_sorting_option("lohi")
    start.assert_prices_are_sorted()
