from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv
from cleaning_links import clean_links
from authentic_brand_filter import authentic_brands

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

print("******Proxy Website**********")
# sometime the actual browser give you the captcha so so cannot then pass that using proxy browser
# Or sometime the website like in this case tiktok creative center blocks the code so use proxy
driver.get("https://plainproxies.com/resources/free-web-proxy/")

# the URL for our intended data
creative_center_url = "https://ads.tiktok.com/business/creativecenter/inspiration/topads/mobile/en?period=30&region=US&industry=22"


print("******Open Creative Center**********")
# scrapping the proxy browser to find the search point and enter our URL
driver.find_element(By.CLASS_NAME, "form-control").click()
driver.find_element(By.CLASS_NAME, "form-control").clear()
driver.find_element(By.CLASS_NAME, "form-control").send_keys(creative_center_url)
time.sleep(1)
driver.find_element(By.CLASS_NAME, "form-control").send_keys(Keys.ENTER)

# A new window will open for our intended browser and maximize it
driver.maximize_window()

print("******Scrapping Creative Center**********")
# print("******Scrapping Creative Center by Brand Name**********")
# time.sleep(180)
time.sleep(30)

# **********************login to creative center****************
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
time.sleep(30)
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

time.sleep(60)
# **********************login to creative center***************
# driver.find_element(By.CLASS_NAME, "byted-select-value").click()
# driver.find_element(By.CLASS_NAME, "byted-select-value").clear()
# # In case of the actual project the **send_keys("loreal")** will be replace by the actual brand name given in Database
# driver.find_element(By.CLASS_NAME, "byted-select-value").send_keys("loreal")
# driver.find_element(By.CLASS_NAME, "byted-select-value").send_keys(Keys.RETURN)
# time.sleep(60)

print("******Getting the links**********")
# the below scrap our intended website and find the classes we want and return the data in object form
parent_element = driver.find_elements(By.XPATH, "//div[contains(@class, 'TopadsVideoCard_cardAction')]")

# maintain a list of the links that we need from the creative center tiktok videos after this stage we will extracting data from that
list_of_links_to_be_scrapped = []

# Taking data from the objects recived
for element in parent_element:
    if len(list_of_links_to_be_scrapped) > 100:
        break
    anchor_element = element.find_element(By.TAG_NAME, "a")
    href_link = anchor_element.get_attribute("href")
    list_of_links_to_be_scrapped.append(href_link)

print(f'List of Links: {list_of_links_to_be_scrapped}')


print("******Scrapping the links**********")
# Storing the data in a CSV file
with open('tiktok_data.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # writer.writerow(['industry', 'brand_name', 'landing_page'])
    for link in list_of_links_to_be_scrapped:
        driver.get(link)

        # Srapping the link
        time.sleep(5)
        elements = driver.find_elements(By.CLASS_NAME, "BasicInfoItem_value__psIua")
        time.sleep(5)

        values = []
        for element in elements:
            # print(element.text)
            values.append(element.text)

        print(values)
        # we remove the extra part after (.com) as we do not need the link for the specific brand we need link for the website
        values = clean_links(values)
        copy_values = values.copy()
        # As we removed the extra part now check if the middle part of the link matches with the name of the brand if yes add it it is an authentic brand else discard it
        simalirity = authentic_brands(copy_values)
        print(values)
        print(simalirity)

        if simalirity >= 0.5:
            if len(values) == 4:
                if values[1] == "-" or values[2] == "-":
                    pass
                else:
                    writer.writerow([values[0], values[1], values[2]])
                    print(f"******Data added for: {link}**********")
            elif len(values) == 5:
                if values[2] == "-" or values[3] == "-":
                    pass
                else:
                    writer.writerow([values[0], values[2], values[3]])
                    print(f"******Data added for: {link}**********")
            elif len(values) == 6:
                if values[3] == "-" or values[4] == "-":
                    pass
                else:
                    writer.writerow([values[1], values[3], values[4]])
                    print(f"******Data added for: {link}**********")
            else:
                pass
        else:
            print("Not An authentic brand")


print("******Scrapping Completed for new brands**********")
time.sleep(3)
driver.quit()
