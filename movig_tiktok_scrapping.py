from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en?period=30&region=PK")
except Exception as e:
    print(str(e))
elem = driver.find_element(By.CLASS_NAME, "byted-select-value")
time.sleep(10)

print(elem)

elem.clear()
elem.send_keys("loreal")
elem.send_keys(Keys.RETURN)
print(elem)


parent_element = driver.find_element(By.CLASS_NAME, "TopadsVideoCard_cardAction__ND3_G")
anchor_element = parent_element.find_element(By.TAG_NAME, "a")
href_link = anchor_element.get_attribute("href")
print(href_link)


input("press a button")
driver.quit()
