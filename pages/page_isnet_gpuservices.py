from playwright.sync_api import Page, expect

class GpuServices_Isnet:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("h1")

    def goto(self):
        self.page.goto("https://www.isnet.net.tr/hizmetlerimiz/veri-merkezi/gpu-as-a-service")


    def verify_gpu_services_page(self):
        expect(self.title).to_have_text("GPU as a Service")