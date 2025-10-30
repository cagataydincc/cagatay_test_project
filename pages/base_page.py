from playwright.sync_api import Page, expect

class Login_Btk:
    def __init__(self, page:Page):
        self.page = page
        self.login_button = page.get_by_role("button", name="Giriş Yap Giriş Yap")
        self.tckn_input = page.get_by_role("textbox", name="TC Kimlik Numarası")
        self.next_button = page.get_by_role("button", name="İleri")
        self.cancel_button = page.get_by_role("button", name="İptal")

    def goto(self):
        self.page.goto("https://www.btkakademi.gov.tr/portal")

    def click_login(self):
        self.login_button.click()

    def fill_tckn(self, tckn: str):
        self.tckn_input.click()
        self.tckn_input.fill('67204021866')

    def click_next(self):
        self.next_button.click()

    def click_cancel(self):
        self.cancel_button.click()
