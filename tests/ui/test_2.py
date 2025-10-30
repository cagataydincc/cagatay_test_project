
from playwright.sync_api import Page
from pages.base_page2 import Login_Isnet   # Eğer ayrı bir dosyada/class'ta tuttuysak

def test_example(page: Page):
    login_page = Login_Isnet(page)
    login_page.goto()
    login_page.click_button()
    login_page.fill_ad()
    login_page.fill_soyad()
    page.wait_for_timeout(10000)

