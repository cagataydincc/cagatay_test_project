import pytest
from playwright.sync_api import sync_playwright


def testlog():
  with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      page = browser.new_page()
      page.goto("https://demo.automationtesting.in/Index.html")
      print("Başarıyla giriş sağlandı.")

"""
#Yukarıdaki kodun aynısı fakat fonksiyon içine page argümanını gönderiyoruz ve bu sayede otomatik runner oluyor
import pytest
from playwright.sync_api import expect

def testlog(page):

      page.goto("https://demo.automationtesting.in/Index.html")
      print("Başarıyla giriş sağlandı.")
"""
