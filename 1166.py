# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("WSR-1166DHPL2(v2) 2.03 インストール & 自動設定スクリプト")
print("> adminのパスワードを入力してEnterキーを押下してください。")
password = input()
# print("> ローカルの1166のファームウェアのフルパスを入力してEnterキーを押下してください。")
print("> 1166のファームウェアを選択してEnterキーを押下してください。")
print("> [1] WSR-1166DHPL2 v1 1.09")
print("> [2] WSR-1166DHPL2 v2 2.03")

# print("> (何も入力せずにEnter押下でデフォルト値が使用されます。)")
# print("> (デフォルト値: C:\\BUFFALO\\wsr1166dhpl2v2-203\\wsr-1166dhpl2v2-203)")
firmware_file_path = input()
if firmware_file_path == "1":
    firmware_file_path = "C:\\BUFFALO\\wsr1166dhpl2-109\\wsr-1166dhpl2-109"
elif firmware_file_path == "2":
    firmware_file_path = "C:\\BUFFALO\\wsr1166dhpl2v2-203\\wsr-1166dhpl2v2-203"

# if firmware_file_path == "":
#     firmware_file_path = "C:\\BUFFALO\\wsr1166dhpl2v2-203\\wsr-1166dhpl2v2-203"

# WebDriverの初期化（Chromeの場合）
# driver_path = "C:/Users/yuki/AppData/Local/Google/Chrome/Application/chromedriver"
# driver_path = "C:\\chromedriver-win64\\chromedriver.exe"
driver_path = "./chromedriver.exe"
driver = webdriver.Chrome(service=ChromeService(driver_path))
# driver = webdriver.Chrome()
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# ルーターのIPアドレス
router_ip = "http://192.168.11.1"

# ログインページにアクセス
driver.get(router_ip)
driver.maximize_window()

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
time.sleep(3)
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
#firmware_file_path = "/path/to/firmware"
time.sleep(5)
driver.find_element(By.NAME, "file").send_keys(firmware_file_path)
time.sleep(10)
driver.find_element(By.NAME, "fwupbutton").click()

# WebDriverを終了
driver.quit()
