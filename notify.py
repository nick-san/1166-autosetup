from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests

# Chromeドライバーのパスを指定
# chrome_driver_path = 'C:\\chromedriver-win64\\chromedriver.exe'

# URLを指定
url = 'https://www.buffalo.jp/product/detail/software/wsr-1166dhpl2.html'

# Chromeドライバーを起動
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# URLにアクセス
driver.get(url)
print("最新ファームウェアのバージョンをチェックしています...")

# ページの読み込みを待機
time.sleep(5)

# 1166 v2 最新バージョン を取得してprint
elements = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/main/div/div/div/div/section[1]/div/div/div/div/div[4]/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[4]')

for elem in elements:

    if float(elem.text) > 2.03:
        isNew = " !New!"
    else:
        isNew = ""

    print("1166 v2: " + elem.text + isNew)

# 1166 v1 最新バージョン を取得してprint
elements = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/main/div/div/div/div/section[1]/div/div/div/div/div[4]/div/div/div/div/div/div/div/div/table/tbody/tr[3]/td[4]')

for elem in elements:

    if float(elem.text) > 1.09:
        isNew = " !New!"
    else:
        isNew = ""

    print("1166 v1: " + elem.text + isNew)

driver.quit()
