from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")

checkbox1=driver.find_element(By.XPATH,"(//input[@type='checkbox'])[1]")
checkbox2=driver.find_element(By.XPATH,"(//input[@type='checkbox'])[2]")

checkbox1.click()
checkbox2.click()

print("Checkbox 1 is selected:", checkbox1.is_selected())
print("Checkbox 2 is selected:", checkbox2.is_selected())

time.sleep(3)
driver.quit()