from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


article_no = driver.find_element(By.CSS_SELECTOR, value = "#articlecount ul li:nth-child(2) a")
article_no.click()



driver.quit()
