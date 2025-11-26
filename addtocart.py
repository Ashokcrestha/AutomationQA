from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

#login
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

time.sleep(2)    #wait for inventory page is loaded

#Add first product to cart
driver.find_element(By.CLASS_NAME,"btn_inventory").click()

time.sleep(1)  # wait a bit for cart badge to appear

# Assert cart badge shows "1"
cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
assert cart_badge == "1", "Cart badge is not 1!"

print("Add to cart assertion passed!")

driver.quit()