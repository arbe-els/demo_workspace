from playwright.sync_api import Page, expect


class StartPage:

    def __init__(self, page:Page):
        self.page = page

        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.locator('[data-test="login-button"]')
        self.swag_labs_logo_locator = page.locator("text=Swag Labs")
        self.error_message_locator = page.locator("[data-test=\"error\"]")


    def open_website(self):
        self.page.goto("https://www.saucedemo.com/")

    def enter_username(self, username: str):
        self.username_field.fill(username)

    def enter_password(self, password: str):
        self.password_field.fill(password)

    def click_login(self):
        self.login_button.click()

    def check_swag_logo_is_visible(self):
        expect(self.swag_labs_logo_locator).to_be_visible()

    def error_message_is_visible(self):
        expect(self.error_message_locator).to_be_visible()

    def error_message_has_correct_text(self):
        expect(self.error_message_locator).to_contain_text(
            "Epic sadface: Sorry, this user has been locked out.")
