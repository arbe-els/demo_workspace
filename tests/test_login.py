from pages.page_start import StartPage


def test_standard_user(page):
    start = StartPage(page)

    start.open_website()
    start.enter_username("standard_user")
    start.enter_password("secret_sauce")
    start.click_login()
    start.check_swag_logo_is_visible()

def test_locked_out_user(page):
    start = StartPage(page)

    start.open_website()
    start.enter_username("locked_out_user")
    start.enter_password("secret_sauce")
    start.click_login()
    start.error_message_is_visible()
    start.error_message_has_correct_text()

def test_problem_user(page):
    start = StartPage(page)

    start.open_website()
    start.enter_username("problem_user")
    start.enter_password("secret_sauce")
    start.click_login()
    start.check_swag_logo_is_visible()

def test_performance_glitch_user(page):
    start = StartPage(page)

    start.open_website()
    start.enter_username("performance_glitch_user")
    start.enter_password("secret_sauce")
    start.click_login()
    start.check_swag_logo_is_visible()

def test_error_user(page):
    start = StartPage(page)

    start.open_website()
    start.enter_username("error_user")
    start.enter_password("secret_sauce")
    start.click_login()
    start.check_swag_logo_is_visible()

def test_visual_user(page):
    start = StartPage(page)

    start.open_website()
    start.enter_username("visual_user")
    start.enter_password("secret_sauce")
    start.click_login()
    start.check_swag_logo_is_visible()
