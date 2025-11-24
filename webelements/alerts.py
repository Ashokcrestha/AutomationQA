from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
time.sleep(1)

alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()  # Click OK

#Confirmation Alert (OK / Cancel)
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
time.sleep(1)

alert = driver.switch_to.alert
print("Confirm Text:", alert.text)
alert.dismiss()  # Click Cancel

# 3️⃣ Prompt Alert (input + OK)
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(1)

alert = driver.switch_to.alert
print("Prompt Text:", alert.text)
alert.send_keys("QA Trainee")
alert.accept()  # Click OK

time.sleep(2)
driver.quit()