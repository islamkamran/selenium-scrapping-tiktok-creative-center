from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

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
creative_center_url = "https://ads.tiktok.com/business/creativecenter/inspiration/topads/mobile/en?period=30&region=US&industry=27"


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
time.sleep(60)
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
    anchor_element = element.find_element(By.TAG_NAME, "a")
    href_link = anchor_element.get_attribute("href")
    list_of_links_to_be_scrapped.append(href_link)

print(f'List of Links: {list_of_links_to_be_scrapped}')


print("******Scrapping the links**********")
# Storing the data in a CSV file
with open('dummy.csv', 'a', newline='') as csvfile:
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
            # if element.text != "":
            #     values.append(element.text)
            # else:
            #     values.append(None)
        # values = [element.text for element in elements]
        print(len(values))
        print(values)

        if len(values) == 4:
            writer.writerow([values[0], values[1], values[2]])
            print(f"******Data added for: {link}**********")
        elif len(values) == 5:
            writer.writerow([values[0], values[2], values[3]])
            print(f"******Data added for: {link}**********")
        elif len(values) == 6:
            writer.writerow([values[1], values[3], values[4]])
            print(f"******Data added for: {link}**********")
        else:
            pass

        # if len(values) == 4:
        #     writer.writerow([values[0], values[1], values[2], values[3]])
        #     print(f"******Data added for: {link}**********")
        # else:
        #     print("Data is less then 4")

print("******Scrapping Completed for new brands**********")
time.sleep(3)
driver.quit()
