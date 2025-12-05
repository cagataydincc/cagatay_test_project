
from playwright.sync_api import Page, expect

class İletisimFormu_İsnet:
    def __init__(self, page:Page):
        self.page = page
        self.input_ad = page.get_by_role("textbox", name="Ad", exact=True)
        self.input_soyad = page.get_by_role("textbox", name="Soyad")
        self.input_sirketadi = page.get_by_role("textbox", name="Şirket Adı")
        self.input_telefonnumber = page.get_by_role("textbox", name="Telefon")
        self.input_email = page.get_by_role("textbox", name="E-posta")
        self.input_aciklama = page.get_by_role("textbox", name="Mesajınız")
        self.kvkk_check1 = page.get_by_role("checkbox", name="Kişisel Verilerin Korunması")
        self.kvkk_check2 = page.get_by_role("checkbox", name="Elektronik Ticari İleti Açık")
        self.button_submit = page.get_by_role("button", name="Gönder")


    def goto(self):
        self.page.goto("https://www.isnet.net.tr/iletisim")

        self.input_ad.fill("TEST")
        self.input_soyad.fill("TEST")
        self.input_sirketadi.fill("TESTFİRMA")
        self.input_telefonnumber.fill("5111111111")
        self.input_email.fill("test@gmail.com")
        self.input_aciklama.fill("TESTAMAÇLIDIRDİKKATEALMAYINIZ")
        self.kvkk_check1.click()
        self.kvkk_check2.click()
        self.button_submit.click()