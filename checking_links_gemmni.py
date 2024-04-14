from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


def clean_url(url):
    # Parse the URL into its components
    url_parts = list(urlsplit(url))

    # Remove any leading or trailing slashes in the path
    url_parts[2] = url_parts[2].strip('/')

    # Remove any extra characters or paths at the beginning or end
    url_parts[2] = url_parts[2].split('/', 1)[0]  # Only keep the first part of the path

    # Reconstruct the cleaned URL
    cleaned_url = urlunsplit(url_parts)
    return cleaned_url


def clean_url2(url):
    # Remove leading and trailing slashes
    cleaned_url = re.sub(r'^/+|/+$', '', url)    
    return cleaned_url


def find_social_links(all_href):
    # This is the default and can be omitted

    social = {} 
    social['facebook'] = "-"
    social['instagram'] = "-"
    social['tiktok'] = "-"
    social['linkedin'] = "-"
    try:
        # grab = requests.get(urls)
        # soup = BeautifulSoup(grab.text, 'html.parser')
    
        # dd
        
        # for link in soup.find_all("a"):
        for link in all_href:
            data = link
            if data:
                if 'facebook' in data:
                    # clean_fb = clean_url(data)
                    # clean_fb= clean_url2(clean_fb)
                    # social['facebook'] = clean_fb
                    social['facebook'] = data
                    
                if 'instagram' in data:
                    # clean_ig = clean_url(data)
                    # clean_ig= clean_url2(clean_ig)
                    # social['instagram'] = clean_ig
                    social['instagram'] = data
                if 'tiktok' in data:
                    # clean_tik = clean_url(data)
                    # clean_tik= clean_url2(clean_tik)
                    # social['tiktok'] = clean_tik
                    social['tiktok'] = data
                if 'linkedin' in data:
                    # clean_linkedin = clean_url(data)
                    # clean_linkedin= clean_url2(clean_linkedin)
                    # social['linkedin'] = clean_linkedin
                    social['linkedin'] = data
        return social
    except:
        return social


def scrape_all_hrefs(url):
  """Scrapes all href links from a website (including iframes) and stores them in a list.

  Args:
      url: The URL of the website to scrape.

  Returns:
      A list of all the scraped href links.
  """

  all_href = []
  driver = webdriver.Chrome()  # Replace with your preferred WebDriver
  driver.maximize_window()
  driver.get(url)

  # Wait for initial page load
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

  # Find all anchor tags (links)
  main_page_links = driver.find_elements(By.TAG_NAME, "a")

  # Iterate through main page links
  for link in main_page_links:
    all_href.append(link.get_attribute("href"))

  # Switch to iframes, if any
  iframes = driver.find_elements(By.TAG_NAME, "iframe")
  for iframe in iframes:
    driver.switch_to.frame(iframe)  # Switch focus to the iframe
    iframe_links = driver.find_elements(By.TAG_NAME, "a")  # Get links inside iframe

    # Iterate through iframe links
    for link in iframe_links:
      all_href.append(link.get_attribute("href"))

    # Switch back to main content
    driver.switch_to.default_content()  # Switch back to main content before proceeding

  driver.quit()
  return all_href

names = ['HealthyBaby','Aura Bora', 'BelliWelli','Kyoot','Happy Cow','Mikey"s"','Ro', 'One Green', 'NEXT HEALTH', 'Taste Salud', 'GVM', 'popl', 'Speechify', 'Latercase', 'HYPER', 'SOUL', 'Ember', 'invideo', 'fairlife', 'KnowSeafood', 'Ellevest', 'Kiinde', 'Skillshare', 'The Futur', 'Trello', 'Klaviyo', 'Evernote', 'Pocket', 'Superhuman', 'Sprout Social', 'Playermaker', 'Imagen', 'LumaTouch', 'Editors Keys', 'Freewell', 'Frame.io', 'Udacity', 'Cleo', 'Padlet', 'FreshBooks', 'Sage', 'Nearpod', 'Quizlet', 'Gong', 'Vidyard', 'Plaito', 'Syte', 'DICE', 'Nothing', 'Starling Bank', 'Prezi', 'Focusmate', 'Meetup', 'Tagged', 'EliteSingles', 'Happn', 'PocketSmith', 'Titan', 'Qapital', 'Monese', 'EarnIn', 'Stash', 'OkCupid', 'Paired', 'Tofurky', 'No Evil Foods', 'Frii Designs', 'DxO Labs', 'Filmic Pro', 'Lumen5', 'InVision', 'Intercom', 'Loom', 'Fitafy', 'Templify', 'Invoke AI', 'GoFlyy', 'Vanguard Photo', 'Greetabl', 'Mealime', 'SNACKLINS', 'Spoonful Of Comfort', 'glonuts', 'Brune', 'Momofuku Goods', 'Japan Candy Store', 'FLY BY JING', 'The Korean Bbq kit', 'Nature"s" Path Organic', 'KIND Snacks', 'Tasty Bite', 'Lovely Candy', 'Neato Robotics', 'OXO', 'Rubbermaid', 'Mmmly', 'Burgess Pet', 'Rosebud', 'Blink', 'Candella', 'Ask AI']

urls = ['https://www.tastybite.co.in', 'https://www.lovelycandystore.com', 'https://www.neatorobotics.com', 'https://www.oxo.com', 'https://www.rubbermaid.com', 'https://www.eatmmmly.com', 'https://www.burgesspetcare.com', 'https://www.rosebud.ai', 'https://www.blink.la', 'https://www.livingwithcandella.com', 'https://www.iask.ai']

# Some websites blocks the scrapping e.g :'https://www.kindsnacks.com',  https://www.naturespath.com https://www.snacklins.com https://www.plaito.ai,'https://www.trello.com',https://www.plaito.ai 'https://www.web.meetcleo.com' 'https://www.editorskeys.com','https://www.frame.io',


for url in urls:
    print(url)
    all_href = scrape_all_hrefs(url)
    if not all_href:
        continue

    # Process or print the list of links
    print(f"Total links found: {len(all_href)}")
    print(all_href)  # Uncomment to print the entire list

    social_links = find_social_links(all_href)
    print(f'social: {social_links}')

    if 'facebook' in social_links:
        print(f"Facebook from social: {social_links['facebook']}")
    if 'tiktok' in social_links:
        print(f"Tiktok from social: {social_links['tiktok']}")
    if 'instagram' in social_links:
        print(f"Insta from social: {social_links['instagram']}")
    if 'linkedin' in social_links:
        print(f"Linkedin from social: {social_links['linkedin']}")

    # Storing the data in a CSV file
    with open('Platforms_links_data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([url, social_links['facebook'], social_links['tiktok'], social_links['instagram'], social_links['linkedin']])
