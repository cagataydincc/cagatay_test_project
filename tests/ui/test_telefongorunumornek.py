import pytest
from playwright.sync_api import sync_playwright



def test_mobile():
    with sync_playwright() as p:
          iphone=p.devices['iPhone 11']
          browser = p.chromium.launch(headless=False)
          context = browser.new_context(**iphone)  # 👈 Emülasyon bu satırda aktifleşiyor
          page = context.new_page()
          # Trace kaydını başlat
          context.tracing.start(screenshots=True, snapshots=True, sources=True)
          page.goto("https://demo.automationtesting.in/Index.html")
          # Trace kaydını durdur ve dosyaya kaydet
          context.tracing.stop(path="trace.zip")

    #tracewiever zip dosyası açmak için=  npx playwright show-trace trace.zip  terminale yaz
    #yeni branch üzerinden ilerleniyor,,