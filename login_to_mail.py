from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

print("******Opening Chrome**********")
# Making options for how to open chrome in which mode
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-notifications")

# Open chrome browser
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://mail.exdnow.com/")
time.sleep(10)
driver.find_element(By.ID, "username").send_keys("islam.kamran@exdnow.com")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("1414@Islam#")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".ZLoginButton").click()
time.sleep(20)
driver.find_element(By.ID, "zlif__CLV-main__-340__pa__0").click()
time.sleep(2)
driver.switch_to.frame(1)
time.sleep(2)
element = driver.find_element(By.CSS_SELECTOR, "div > p")
text = element.text
print(text)

input("Press Enter")
driver.quit()
