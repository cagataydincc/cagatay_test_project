import requests
import time

URL = "https://www.isnet.net.tr/"  # Kontrol etmek istediğin sitenin adresi
INTERVAL = 1 * 60  # 5 dakika = 300 saniye

while True:
    try:
        response = requests.get(URL, timeout=10)
        if response.status_code == 200:
            print(f"{time.ctime()}: {URL} çalışıyor.")
        else:
            print(f"{time.ctime()}: Hata kodu: {response.status_code}")
    except Exception as e:
        print(f"{time.ctime()}: Erişim hatası: {e}")

    time.sleep(INTERVAL)  # 1 dakika bekle, sonra tekrar dene
