from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://python.org")



events = driver.find_elements(By.XPATH, value = '/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li')
bigger_store = {}
i = 0 
for event in events:
    date_raw = event.find_element(By.TAG_NAME, value='time').get_attribute('datetime')
    name = event.find_element(By.TAG_NAME, value='a').text
    date = date_raw.split('T')
    store = {'time':date[0],
             'name':name}
    bigger_store[i] = store.copy()
    key, value = store.popitem()
    i = i + 1
print(bigger_store)

#print(bigger_store)
#documentation_driver = driver.find_element(By.CSS_SELECTOR, value = '.documentation-widget a')

#print(documentation_driver.text)

#submit_web = driver.find_element(By.XPATH, value='/html/body/div/footer/div[2]/div/ul/li[3]/a')

#print(submit_web.text)


driver.quit()
