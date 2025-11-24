from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID,"user-name")
username.send_keys("standard_user")

password = driver.find_element(By.XPATH,"//input[@data-test='password']")
password.send_keys("secret_sauce")

login = driver.find_element(By.CSS_SELECTOR,'#login-button')
login.click()
print("Login Successfull")
time.sleep(5)