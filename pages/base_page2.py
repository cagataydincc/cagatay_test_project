from playwright.sync_api import Page, expect

class Login_Isnet:
    def __init__(self, page:Page):
        self.page = page
        self.destek_button = page.get_by_role("link", name="Destek")
        self.ad_input = page.locator('input[placeholder="Adınız"]')
        self.soyad_input = page.locator('input[placeholder="Soyadınız"]')


    def goto(self):
        self.page.goto("https://www.isnet.net.tr/")

    def click_button(self):
        self.destek_button.click()

    def fill_ad(self):

        self.ad_input.fill('CAGATAYTEST')

    def fill_soyad(self):

        self.soyad_input.fill('DİNCTEST')


