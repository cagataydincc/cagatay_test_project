from playwright.sync_api import Page
from pages.page_isnet_gpuservices import GpuServices_Isnet   # Eğer ayrı bir dosyada/class'ta tuttuysak

def test_gpu_services_page(page: Page):
    gpu_services_page = GpuServices_Isnet(page) # GpuServices_Isnet classını tanımladık ona görede aşağıda fonksiyonları çağırdık
    gpu_services_page.goto()
    gpu_services_page.verify_gpu_services_page()
    page.wait_for_timeout(500)