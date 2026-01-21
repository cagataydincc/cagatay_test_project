
from playwright.sync_api import Page
from pages.page_isnet_destekformu import Login_Isnet   # Eğer ayrı bir dosyada/class'ta tuttuysak


def test_example(page: Page):
    login_page = Login_Isnet(page) #login_Isnet classını tanımladık ona görede aşağıda fonksiyonları çağırdık
    login_page.goto()
    login_page.click_button()
    login_page.fill_ad("TEST")
    login_page.fill_soyad("TESTER")
    login_page.fill_sirketadi("TEST ŞİRKETİ")
    login_page.fill_phoneNumber("5111111111")
    login_page.fill_email("test@hotmail.com")
    login_page.fill_aciklama("Bu bir test mesajıdır.")
    login_page.checkbox_kvk()
    login_page.checkbox_kvkk2()
    #login_page.checkbox_captcha()  -- CAPTCHA KONTROLU BYPASS EDİLMELİ
    login_page.button_gonderme()
    page.wait_for_timeout(10000)

