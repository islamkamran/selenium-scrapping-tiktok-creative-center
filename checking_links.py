import re
from urllib.parse import urlsplit, urlunsplit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from pyvirtualdisplay import Display
import time



def get_all_data(driver):

    # Initialize lists to store all href attributes and content
    all_hrefs = []
    all_list_data = []

    # Function to recursively get href attributes and list data from iframes
    def get_iframe_data(frame):
        driver.switch_to.frame(frame)
        
        # Get href attributes
        iframe_hrefs = driver.find_elements(By.XPATH, "//a[@href]")
        all_hrefs.extend([link.get_attribute("href") for link in iframe_hrefs])
        
        # Get content inside ul and li tags
        iframe_lists = driver.find_elements(By.XPATH, "//ul|//li")
        all_list_data.extend([element.text for element in iframe_lists])
        
        # Recursively check if there are nested iframes
        nested_iframes = driver.find_elements(By.TAG_NAME, "iframe")
        for nested_frame in nested_iframes:
            get_iframe_data(nested_frame)
        
        driver.switch_to.default_content()

    # Get href attributes and list data from the main document
    main_hrefs = driver.find_elements(By.XPATH, "//a[@href]")
    all_hrefs.extend([link.get_attribute("href") for link in main_hrefs])
    
    main_lists = driver.find_elements(By.XPATH, "//ul|//li")
    all_list_data.extend([element.text for element in main_lists])

    # Get href attributes and list data from iframes
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    for frame in iframes:
        get_iframe_data(frame)

    # Get href attributes and list data from footer
    footer_hrefs = driver.find_elements(By.XPATH, "//footer//a[@href]")
    all_hrefs.extend([link.get_attribute("href") for link in footer_hrefs])
    footer_lists = driver.find_elements(By.XPATH, "//footer//ul|//footer//li")
    all_list_data.extend([element.text for element in footer_lists])
    short_list = []

    if all_hrefs:
        for elem in all_hrefs:

            if 'facebook' in str(elem).lower() or 'tik' in str(elem).lower() or 'linkedin' in str(elem).lower() or 'instagram'  in str(elem).lower():
                short_list.append(elem)

    return short_list


def scrape_links_with_selenium(url):
    print(1)

    # Set up the Selenium WebDriver with Chrome
    final_data = []
    stringy_data = ""
    df_links = None
    # Set up Chrome options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-notifications")
    print(2)


    # display = Display(visible=0, size=(800, 600))
    print(3)
    # display.start()
    all_hrefs = []
    # Create a webdriver instance
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    # Set a delay between requests
    delay_seconds = 10
    driver.maximize_window()
    print(4)


    try:
        # Navigate to the URL
        value= None
        main_page=""
        print(5)
        # new tab
        # driver.execute_script("window.open('');")
        # driver.switch_to.window(driver.window_handles[-1])

        driver.get(url)
        time.sleep(delay_seconds)
        print(6)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(7)

        time.sleep(delay_seconds)

        # Perform any interactions or wait for elements to load if needed

        # Get all links on the page
        main_page = (driver.find_element(By.XPATH, "/html/body").text)
        print(8)

        time.sleep(delay_seconds)



        main_page = main_page.replace('\n', ' ').replace('\t', ' ')
        print(9)
        print(f'The main Page: {main_page}')

    # return main_page
        links = get_all_data(driver)
        # print(f'links after main: {links}')

        if links:
            links = list(set(links))
            df_links=', '.join(links)

        stringy_data += main_page
        print(8)

        final_data.append(main_page)
        print(9)
        # Initialize lists to store all href attributes and content
        all_hrefs = []
        all_list_data = []

        # Function to recursively get href attributes and list data from iframes
        def get_iframe_data(frame):
            driver.switch_to.frame(frame)

            # Get href attributes
            driver.implicitly_wait(5)

            # iframe_hrefs = driver.find_elements(By.XPATH, "//a[@href]")
            iframe_hrefs = driver.find_elements(By.XPATH, "//a[@href and string-length(@href) > 0]")  # this could be alternate approach for finding the href more preciously
            print(10)
            all_hrefs.extend([link.get_attribute("href") for link in iframe_hrefs])

            # Get content inside ul and li tags
            iframe_lists = driver.find_elements(By.XPATH, "//ul|//li")
            print(11)
            all_list_data.extend([element.text for element in iframe_lists])
            print(12)
            # Recursively check if there are nested iframes
            nested_iframes = driver.find_elements(By.TAG_NAME, "iframe")
            print(13)
            for nested_frame in nested_iframes:
                get_iframe_data(nested_frame)
            
            driver.implicitly_wait(2)
            driver.switch_to.default_content()
            print(14)
            # may be like at this point we need to go out of the frame

        # Get href attributes and list data from the main document
        print(15)
        # main_hrefs = driver.find_elements(By.XPATH, "//a[@href]")
        main_hrefs = driver.find_elements(By.XPATH, "//a[@href and string-length(@href) > 0]")  # this could be alternate approach for finding the href more preciously

        all_hrefs.extend([link.get_attribute("href") for link in main_hrefs])
        print(16)
        main_lists = driver.find_elements(By.XPATH, "//ul|//li")
        all_list_data.extend([element.text for element in main_lists])

        # Get href attributes and list data from iframes
        print(17)
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        print(18)
        for frame in iframes:
            get_iframe_data(frame)
        print(19)
        # Get href attributes and list data from footer
        # footer_hrefs = driver.find_elements(By.XPATH, "//footer//a[@href]")
        footer_hrefs = driver.find_elements(By.XPATH, "//footer//a[@href and string-length(@href) > 0]")  # this could be alternate approach for finding the href more preciously
        all_hrefs.extend([link.get_attribute("href") for link in footer_hrefs])
        print(20)
        footer_lists = driver.find_elements(By.XPATH, "//footer//ul|//footer//li")
        all_list_data.extend([element.text for element in footer_lists])
        print(21)

        href_links = []

        elems = driver.find_elements(by=By.XPATH, value="//a[@href and string-length(@href) > 0]")
        print(22)
        
        if elems:
            print(23)
            for elem in elems:
                l = elem.get_attribute("href")
                if l not in href_links:
                    if 'contact' in str(l).lower() or 'about' in str(l).lower() or 'network' in str(l).lower() or 'story' in str(l).lower() :
                        href_links.append(l)
        else:
            print(24)
            href_elements = driver.find_elements(By.TAG_NAME, "a")

            # Filter for elements with an href attribute
            href_links = [elem for elem in href_elements if elem.get_attribute("href")]
        print(25)
        if len(href_links) > 3:
            print(26)
            href_links = href_links[:3]
        print(27)
        for url in href_links:

            driver.execute_script("window.open('', '_blank');")
            time.sleep(delay_seconds)
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(delay_seconds)
            # Load the URL in the new tab
            print(28)
            driver.get(url)
            print(29)
            time.sleep(delay_seconds)
            try:
                print(30)
                sub_page = (driver.find_element(By.XPATH, "/html/body").text)
                print("30A")
                if sub_page:
                    stringy_data += sub_page
                driver.implicitly_wait(6)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except:
                continue
                print("********************Har dafa close karta hai?****************8")
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

        print(31)
        # driver.close()
        # driver.switch_to.window(driver.window_handles[0])
        print(32)  # this will check if after closing the tab still it returns the data or not
        driver.close()
        return stringy_data, main_page, all_hrefs
    except:
        # driver.close()
        # driver.switch_to.window(driver.window_handles[0])
        print(33)
        driver.close()
        return "", main_page, all_hrefs


stringify_data, main_page, all_href = scrape_links_with_selenium("https://www.healthybaby.com/")
# stringify_data, main_page, all_href = scrape_links_with_selenium(brand_to_scrape.web_url)

print(f"Stringify: {stringify_data}")
print(f"main page: {main_page}")
print(f"all href: {all_href}")
