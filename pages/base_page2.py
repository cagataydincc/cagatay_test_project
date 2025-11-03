from playwright.sync_api import Page, expect
#Önce locatorler tanımlanır daha sonra yapacakları işlemler
class Login_Isnet:
    def __init__(self, page:Page):
        self.page = page
        self.destek_button = page.get_by_role("link", name="Destek")
        self.ad_input = page.locator('input[placeholder="Adınız"]')
        self.soyad_input = page.locator('input[placeholder="Soyadınız"]')
        self.sirketadi_input = page.get_by_role("textbox", name="Şirket Adı")
        self.phoneNumber_input = page.get_by_role("textbox", name="Telefon")
        self.email_input = page.get_by_role("textbox", name="E-posta")
        self.aciklama_input = page.get_by_role("textbox", name="Mesajınız")
        self.kvkk_checkbox = page.get_by_role("checkbox", name="Kişisel Verilerin Korunması")
        self.kvkk2_checkbox =  page.get_by_role("checkbox", name="Elektronik Ticari İleti Açık")
       #self.captcha_checkbox = page.locator("iframe[name=\"a-49wdudm94mpq\"]").content_frame.get_by_role("checkbox", name="Ben robot değilim")
        self.gonder_button = page.get_by_role("button", name="Gönder")










    def goto(self):
        self.page.goto("https://www.isnet.net.tr/")

    def click_button(self):
        self.destek_button.click()

    def fill_ad(self):

        self.ad_input.fill('CAGATAYTEST')

    def fill_soyad(self):

        self.soyad_input.fill('DİNCTEST')

    def fill_sirketadi(self):
        self.sirketadi_input.fill("TESTFİRMA")

    def fill_phoneNumber(self):
        self.phoneNumber_input.fill('5324645159')

    def fill_email(self):
        self.email_input.fill("test@gmail.com")

    def fill_aciklama(self):
        self.aciklama_input.fill("TEST AMAÇLIDIR DİKKATE ALMAYINIZ")

    def checkbox_kvk(self):
        self.kvkk_checkbox.click()

    def checkbox_kvkk2(self):
        self.kvkk2_checkbox.click()

   #def checkbox_captcha(self): -- CAPTCHA KONTROLU BYPASS EDİLMELİ
    #   self.captcha_checkbox.click()

    def button_gonderme(self):
        self.gonder_button.click()