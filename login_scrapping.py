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
driver.get("https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en?period=30&region=US")

time.sleep(10)
driver.find_element(By.CLASS_NAME, "FixedHeaderPc_loginBtn__lL73Y").click()
time.sleep(10)
driver.find_element(By.CLASS_NAME, "LoginSelection_loginImg__M_8xx").click()
time.sleep(5)
driver.find_element(By.ID, "TikTok_Ads_SSO_Login_Email_Input").click()
driver.find_element(By.ID, "TikTok_Ads_SSO_Login_Email_Input").send_keys("islam.kamran@exdnow.com")
time.sleep(1)
driver.find_element(By.ID, "TikTok_Ads_SSO_Login_Pwd_Input").click()
driver.find_element(By.ID, "TikTok_Ads_SSO_Login_Pwd_Input").send_keys("movig@123")
time.sleep(2)
driver.find_element(By.ID, "TikTok_Ads_SSO_Login_Btn").click()
time.sleep(15)
# driver.find_element(By.CLASS_NAME, "secsdk_captcha_refresh refresh-button").click()
# driver.find_element(By.CSS_SELECTOR, ".secsdk_captcha_refresh--text").click()
driver.find_element(By.CSS_SELECTOR, ".verify-captcha-submit-button").click()

time.sleep(30)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[-1])
driver.get("https://mail.exdnow.com/")
time.sleep(10)
driver.find_element(By.ID, "username").send_keys("islam.kamran@exdnow.com")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("1414@Islam#")
time.sleep(2)
# By.XPATH, "//div[contains(@id, 'zlif__CLV-main')]
driver.find_element(By.CSS_SELECTOR, ".ZLoginButton").click()
time.sleep(20)
the_data = driver.find_elements(By.XPATH, "(//div[contains(@id, 'zlif__CLV-main')])[1]")
print(f"the data is:{the_data}")
the_data[0].click()

# driver.find_element(By.CLASS_NAME, "ZmRowDoubleHeader Unread").click()
time.sleep(2)
driver.switch_to.frame(1)
time.sleep(2)
element = driver.find_element(By.CSS_SELECTOR, "div > p")
text = element.text
print(text)

driver.close()

driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
driver.find_element(By.ID, "TikTok_Ads_SSO_Login_Code_Input").click()
driver.find_element(By.ID, "TikTok_Ads_SSO_Login_Code_Input").send_keys(text)
driver.find_element(By.NAME, "CodeloginBtn").click()

input("press enter")

driver.quit()
