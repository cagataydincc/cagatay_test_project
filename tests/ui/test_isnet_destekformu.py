
from playwright.sync_api import Page
from pages.page_isnet_destekformu import Login_Isnet   # Eğer ayrı bir dosyada/class'ta tuttuysak


def test_example(page: Page):
    login_page = Login_Isnet(page)
    login_page.goto()
    login_page.click_button()
    login_page.fill_ad()
    login_page.fill_soyad()
    login_page.fill_sirketadi()
    login_page.fill_phoneNumber()
    login_page.fill_email()
    login_page.fill_aciklama()
    login_page.checkbox_kvk()
    login_page.checkbox_kvkk2()
    #login_page.checkbox_captcha()  -- CAPTCHA KONTROLU BYPASS EDİLMELİ
    login_page.button_gonderme()
    page.wait_for_timeout(10000)

