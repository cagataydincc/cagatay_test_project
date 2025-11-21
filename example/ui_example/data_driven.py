import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize("username,password",
                         [
                             ("Admin", "admin123"),#TRUE KULLANICI ADI ŞİFRE
                             ("user1","password1"),#FALSE KULLANICI ADI ŞİFRE
                             ("", ""),
                         ]
)  #DATA DRİVEN TEST İÇİN, SAYFAYI HEM DOĞRU BİLGİLERLE HEM YANLIŞ BİLGİLERLE TEST EDİYOR.
def testlog51(username,password):
  with sync_playwright() as p:
      browser = p.chromium.launch(headless=False,slow_mo=1000)
      page = browser.new_page()
      page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
      page.get_by_role("textbox", name="Username").click()
      page.get_by_role("textbox", name="Username").fill(username)
      page.get_by_role("textbox", name="Password").click()
      page.get_by_role("textbox", name="Password").fill(password)
      page.get_by_role("button", name="Login").click()

