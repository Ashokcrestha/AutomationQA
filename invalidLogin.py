from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID,"user-name")
username.send_keys("wrong_user")

password = driver.find_element(By.NAME,"password")
password.send_keys("secrets_sauce")

login = driver.find_element(By.CSS_SELECTOR,'#login-button')
login.click()
print("Username and Password are wrong/unmatched")
time.sleep(5)