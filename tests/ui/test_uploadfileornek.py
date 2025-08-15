from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(record_video_dir='./video')
    page.goto('https://demo.automationtesting.in/FileUpload.html')
    page.wait_for_timeout(1000)


    #Dosya yükleme fonksiyonu
    file_upload='./deneme.py'
    upload_location = page.query_selector('#input-4')
    upload_location.set_input_files(file_upload)
    page.wait_for_timeout(1000)
    page.screenshot(path='./video/test.png')#ekran göruntusu alma