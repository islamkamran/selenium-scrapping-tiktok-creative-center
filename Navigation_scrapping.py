from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://google.com")

elem = driver.find_element(By.ID, "APjFqb")
elem.clear()
elem.send_keys("islam kamran")
store = elem.send_keys(Keys.RETURN)
store.find_element()
input("press a key")
driver.quit()
