from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#implicit wait 
driver.implicitly_wait(5)   # wait up to 5 sec for any elements

driver.get("https://www.amazon.com/")

# find search box and type
search = driver.find_element(By.ID,"twotabsearchtextbox") 
search.send_keys("laptop")

# click search button
driver.find_element(By.ID,"nav-search-submit-button").click()

print("Implicit wait success!")

driver.quit()