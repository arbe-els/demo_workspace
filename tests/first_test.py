from playwright.sync_api import sync_playwright

with sync_playwright() as p:
   browser = p.chromium.launch(headless=True)
   page = browser.new_page()
   page.goto('https://google.com')
   print("The title of the given page is:", page.title())
   browser.close()