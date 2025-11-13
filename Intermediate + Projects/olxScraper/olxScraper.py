from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = uc.ChromeOptions()
driver = uc.Chrome(options=chrome_options)

driver.get("https://www.olx.com.pk/mobile-phones_c1453")

wait = WebDriverWait(driver,10)
listings = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul/li[.//div[@aria-label='Title']]")))
listing_cards = []
for listing in listings:
    listing_cards.append(listing)
#
listing_cards[1].click()
 

def scraping_item():
    wait = WebDriverWait(driver,10)

    title = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1'))
    ).text 
    price =  wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'span[aria-label="Price"]'))
    ).text

    image = wait.until(
        EC.presence_of_element_located((  By.XPATH, '/html/body/div[2]/div[2]/header[2]/div/div[1]/div/div[4]/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/picture/img'))
    )
    description_div = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[div[text()="Description"]]/div[2]/span' ))
    ).text
    img_url = image.get_attribute('src')
    data =  {"title":title,
             "price":price,
             "desc":description_div,
             "img":img_url}
              
    return data


   

 # for listing in listings:
#     title = listing.find_element(By.XPATH, './/div[@aria-label="Title"]').text
#     price = listing.find_element(By.XPATH, './/div[@aria-label="Price"]').text
#     print(title, price)

