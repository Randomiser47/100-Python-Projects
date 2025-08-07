from selenium import webdriver
from selenium.webdriver.common.by import By








driver = webdriver.Chrome()

driver.get("https://mistore.pk/products/xiaomi-pad-7-pro-12gb-512gb?variant=41109582250064")

price = driver.find_element(By.XPATH, value="/html/body/main/section[1]/product-info/div/div/div[2]/section/div[2]/div/div/div[1]/span[2]")
print(price.text)
