from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/")

wait = WebDriverWait(driver,10)

#wait for search box to be visible

search = wait.until(EC.visibility_of_element_located((By.ID,"twotabsearchtextbox")))
search.send_keys("laptop")

#wait for search button to be clickable
button = wait.until(EC.element_to_be_clickable((By.ID,"nav-search-submit-button")))
button.click()

#wait for page title to contain "laptop"
wait.until(EC.title_contains("laptop"))

#assertion
assert "laptop" in driver.title.lower(), "Serach result not loaded"

print("Explict wait and assertion both succesfully")

driver.quit()