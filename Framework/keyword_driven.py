from selenium import webdriver 
from selenium.webdriver.common.by import By
import csv, time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

def perform_action(keyword, locator, value):
    element = driver.find_element(By.ID, locator)

    if keyword == "enterText":
        element.send_keys(value)
    elif keyword == "click":
        element.click()

with open("Framework/keywords.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        perform_action(row["keyword"], row["locator"], row["value"])
                       

time.sleep(2)
driver.quit()
