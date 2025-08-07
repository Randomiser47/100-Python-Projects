from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 
import time
import undetected_chromedriver as uc 

chrome_options = uc.ChromeOptions()

driver = uc.Chrome(options = chrome_options)
driver.get('https://orteil.dashnet.org/cookieclicker/')
################################# finding elements ##################
time.sleep(5)
english = driver.find_element(By.ID,value='langSelect-EN')
english.click()
time.sleep(5)
################################# Code ############################3
start_time = time.perf_counter()
down_time = time.perf_counter()
button = driver.find_element(By.ID, value="bigCookie")
button_press = True
while button_press == True:
   button.click() 
   products = driver.find_elements(By.CSS_SELECTOR, value="div[id^='product']")
   best_item = None
   for product in reversed(products):
       if "enabled" in product.get_attribute("class"):
                best_item = product
                break
   if best_item:
            best_item.click()
            start_time = time.perf_counter()    
   if time.perf_counter() - down_time >= 300:
            break
print('program has ended')
time.sleep(1)

