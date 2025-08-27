from playwright.sync_api import Page, expect


class HomePage:

    def __init__(self, page:Page):
        self.page = page

        self.product_price_locator = page.locator('[data-test="inventory-item-price"]')
        self.add_to_cart = page.locator('[data-test="add-to-cart"]')
        self.shopping_cart_locator = page.locator('[data-test="shopping-cart-badge"]')
        self.back_to_products = page.locator('[data-test="back-to-products"]')
        self.swag_labs_logo_locator = page.locator("text=Swag Labs")
        self.dropdown_locator = page.locator('[data-test="product-sort-container"]')
        self.extract_prices_text = page.locator(".inventory_item_price")


    def click_product_select(self, product_name: str):
        return self.page.locator(f"text={product_name}").click()

    def product_price_check(self, product_price: str):
        expect(self.product_price_locator).to_contain_text(f"{product_price}")

    def click_add_to_cart(self):
        self.add_to_cart.click()

    def cart_amount_check(self, amount_in_cart: str):
        expect(self.shopping_cart_locator).to_contain_text(f"{amount_in_cart}")

    def click_back_to_products(self):
        self.back_to_products.click()

    def check_swag_logo_is_visible(self):
        expect(self.swag_labs_logo_locator).to_be_visible()

    def click_sorting_dropdown(self):
        self.dropdown_locator.click()

    def click_sorting_option(self, sorting_option: str):
        self.dropdown_locator.select_option(f"{sorting_option}")

    def assert_prices_are_sorted(self):
        prices = self.extract_prices_text.all_text_contents()
        self.prices = [float(price.strip().replace("$", "")) for price in prices]
        assert self.prices == sorted(self.prices)
