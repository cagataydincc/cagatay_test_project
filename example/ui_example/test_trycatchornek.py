import pytest
from playwright.sync_api import sync_playwright, expect

def test_trycatchornek():
   with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(record_video_dir='./video')
    page.goto('https://demo.automationtesting.in/Selectable.html')
    page.wait_for_timeout(1000)
    try:
        elements = page.query_selector_all('tght')
        print(len(elements))
        for i in elements:
            print(i.text_content())
        page.wait_for_timeout(1000)

    except Exception as e:
        print("⛔ Sayfa yüklenirken beklenmeyen bir hata oluştu:", str(e))
