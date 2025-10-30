import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        print("Bağlantı kapatıldı")
        browser.close()


def test_login(browser):

        page = browser.new_page()
        page.goto('https://demo.automationtesting.in/Index.html')
        print("Test 1 çalışıyor")

def test_google_translate(browser):

        page = browser.new_page()
        page.goto('https://translate.google.com/?hl=tr&sl=en&tl=tr&op=translate')
        print("Test 2 çalışıyor")
