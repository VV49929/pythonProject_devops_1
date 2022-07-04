import selenium.common.exceptions
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/israeltesler/Downloads/chromedriver")

driver.get("http://localhost:5001/users/14")
driver.implicitly_wait(5)
print(driver.current_url)
print(driver.title)
print(driver.page_source)
#driver.quit()
try:
    elenent = driver.find_element(by=By.ID,value="user")
    print(elenent.is_enabled())
    print(elenent.text)
except selenium.common.exceptions.NoSuchElementException:
    elenent = driver.find_element(by=By.ID, value="error")
    print(elenent.is_enabled())
    print(elenent.text)
#driver.quit()
