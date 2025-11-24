from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#1. open chrome browser
driver = webdriver.Chrome()

#2.go to google
driver.get("https://www.google.com")

import time
time.sleep(5)
driver.quit()
print("driver closed")