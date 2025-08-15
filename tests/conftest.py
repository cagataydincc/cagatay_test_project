import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    # Playwright başlat
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
