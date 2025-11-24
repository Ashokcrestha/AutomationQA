from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username  = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.ID,"password")
login = driver.find_element(By.ID,"login-button")
#login = driver.find_element(By.XPATH,"//input[@id="login-button"]")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
print("password entered")
login.click()
time.sleep(5)

addtocart = driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")

addtocart.click()
time.sleep(5)

shop = driver.find_element(By.CLASS_NAME,"shopping_cart_container")
shop.click()
time.sleep(5)

checkout = driver.find_element(By.ID,"checkout")
checkout.click()
time.sleep(5)

fname  = driver.find_element(By.ID,"first-name")
fname.send_keys("Ashok")

lname =driver.find_element(By.ID,"last-name")
lname.send_keys("Shrestha")

postalcode = driver.find_element(By.ID,"postal-code")
postalcode.send_keys("1235")
time.sleep(10)

Continue = driver.find_element(By.ID,"continue")
Continue.click()
time.sleep(5)