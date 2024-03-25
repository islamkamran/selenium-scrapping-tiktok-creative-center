from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en?period=30&region=PK&industry=22")
time.sleep(5)
driver.find_element(By.CLASS_NAME, "FixedHeaderPc_loginBtn__lL73Y").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "GoogleLoginButton_googleLogo__GTKvn").click()

input("press enter")

driver.quit()
