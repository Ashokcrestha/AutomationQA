from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

#Simple Assert - check page title
assert driver.title == "Swag Labs", "Title is wrong!"

print("Title assertion passed!")

#Enter username & password
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")

#click login
driver.find_element(By.ID,"login-button").click()
time.sleep(2)

#Simple Assert - check login success using URL
assert "inventory" in driver.current_url, "Login failed"

print("Login assertion passed!")

driver.quit()
