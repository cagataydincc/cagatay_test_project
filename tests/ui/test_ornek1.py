
from playwright.sync_api import Page
from pages.base_page import Login_Btk   # Eğer ayrı bir dosyada/class'ta tuttuysak

def test_example(page: Page):
    login_page = Login_Btk(page)
    login_page.goto()
    login_page.click_login()
    login_page.fill_tckn("67204021866")
    login_page.click_next()
    login_page.click_cancel()

