
from playwright.sync_api import Page
from pages.page_isnet_iletisimformu  import İletisimFormu_İsnet   # Eğer ayrı bir dosyada/class'ta tuttuysak

def test_example(page: Page):
    login_page = İletisimFormu_İsnet(page)
    login_page.goto()
    page.wait_for_timeout(10000)
