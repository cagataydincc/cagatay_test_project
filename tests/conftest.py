import sys
import os
import pytest
from playwright.sync_api import sync_playwright

# --------------------------------------------------
# Proje kök dizinini Python path'e ekle
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PROJECT_ROOT)
sys.path.append(os.path.abspath(os.path.join(PROJECT_ROOT, "..")))  # bir üst klasör
# --------------------------------------------------

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
