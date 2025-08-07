from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
import undetected_chromedriver as uc

# Configure Chrome options
chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Initialize the driver
driver = uc.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/cookieclicker/')

try:
    # Wait for and select the English language
    try:
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, 'langSelect-EN'))
        ).click()
        # Wait for the game to load after language selection
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, 'bigCookie'))
        )
    except TimeoutException:
        print("Language selection or game load timed out. Continuing anyway...")

    # Main loop
    start_time = time.perf_counter()
    down_time = time.perf_counter()
    while time.perf_counter() - down_time < 300:  # Run for 5 minutes
        try:
            # Re-fetch the bigCookie to avoid stale references
            button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, 'bigCookie'))
            )
            button.click()  # Click the big cookie

            # Find all enabled products
            products = driver.find_elements(By.CSS_SELECTOR, "div[id^='product'].enabled")
            if products:
                try:
                    products[-1].click()  # Click the most expensive enabled product
                except StaleElementReferenceException:
                    print("Stale product detected, retrying...")
                    continue

        except (StaleElementReferenceException, TimeoutException) as e:
            print(f"Error during clicking: {e}")
            time.sleep(0.1)  # Brief pause to avoid rapid error looping

    print("Program has ended")

finally:
    # Clean up
    time.sleep(1)
    driver.quit()
