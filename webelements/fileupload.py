from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")

fileupload = driver.find_element(By.ID,"file-upload")
fileupload.send_keys("E:\QA CLASS\Assignment1.docx")

driver.find_element(By.ID,"file-submit").click()

time.sleep(5)
driver.quit()