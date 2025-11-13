
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = uc.ChromeOptions()
driver = uc.Chrome(options=chrome_options)

driver.get("https://www.olx.com.pk/mobile-phones_c1453")

wait = WebDriverWait(driver,10)
listings = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul/li[.//div[@aria-label='Title']]")))

def scrape_main_page():
    all_data = []
    listings = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//ul/li[.//div[@aria-label='Title']]")
        )
    )

    for listing in listings:
        try:
            title = listing.find_element(By.XPATH, './/div[@aria-label="Title"]').text
            price = listing.find_element(By.XPATH, './/div[@aria-label="Price"]').text
            img = listing.find_element(By.TAG_NAME, 'img').get_attribute('src')

            all_data.append({
                "title": title,
                "price": price,
                "img": img
            })
        except:
            continue

    return all_data

