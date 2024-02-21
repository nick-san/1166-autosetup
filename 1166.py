from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

print("WSR-1166DHPL2(v2) 2.03 インストール & 自動設定スクリプト")
print("> adminのパスワードを入力してEnterキーを押下してください。")
password = input()
print("> ローカルの1166のファームウェアのフルパスを入力してEnterキーを押下してください。")
#firmware_file_path = "/home/nick/Downloads/wsr1166dhpl2v2-203/wsr-1166dhpl2v2-203"
firmware_file_path = input()

# WebDriverの初期化（Chromeの場合）
driver = webdriver.Chrome()

# ルーターのIPアドレス
router_ip = "http://192.168.11.1"

# ログインページにアクセス
driver.get(router_ip)

# ログイン情報
#password = "4hbkmx3b"

# ログインフォームにユーザー名とパスワードを入力して送信
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_nosave_Password")))
password_input.send_keys(password)
time.sleep(3)
driver.find_element(By.ID, "id_login").click()

# ログイン後、設定画面に移動
driver.get("http://192.168.11.1/index_adv.html")

# DHCPサーバーからの自動取得に変更
driver.switch_to.default_content()
driver.find_element(By.ID, "AT_WAN").click()
driver.find_element(By.ID, "sub_meu1_0").click()
time.sleep(3)
driver.switch_to.frame("content_main")
driver.find_element(By.ID, "id_WanMethod1").click()
driver.find_element(By.ID, "wan_apply").click()
time.sleep(3)
WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.ID,"routeron")))
driver.switch_to.default_content()

# IPv6を無効化
driver.switch_to.default_content()
driver.find_element(By.ID, "sub_meu1_3").click()
time.sleep(3)
driver.switch_to.frame("content_main")
driver.find_element(By.ID, "id_IPv6Method1").click()
driver.find_element(By.CLASS_NAME, "button22").click()
time.sleep(3)
WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.ID,"routeron")))
driver.switch_to.default_content()

# ファームウェアアップデート
# 例：ファームウェアファイルのパスを指定してアップデート
driver.find_element(By.ID, "AT_ADMIN").click()
driver.find_element(By.ID, "sub_meu6_3").click()
time.sleep(3)
driver.switch_to.frame("content_main")
#firmware_file_path = "/home/nick/Downloads/wsr1166dhpl2v2-203/wsr-1166dhpl2v2-203"
time.sleep(5)
driver.find_element(By.NAME, "file").send_keys(firmware_file_path)
time.sleep(10)
driver.find_element(By.NAME, "fwupbutton").click()

# WebDriverを終了
driver.quit()
