from selenium import webdriver 
from selenium.webdriver.common.by import By
import csv, time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

with open("Framework/testdata.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:

        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "user-name").send_keys(row["username"])
        driver.find_element(By.ID, "password").send_keys(row["password"])
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(2)

driver.quit()