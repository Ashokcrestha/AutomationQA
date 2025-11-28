from selenium import webdriver
from loginpage import LoginPage

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

login_page = LoginPage(driver)
login_page.login("standard_user", "secret_sauce")

#wait for inventory page to load
inventory_url = "inventory.html"
if inventory_url in driver.current_url:
    print("Login successful!")
else:
    print("Login failed!")

driver.quit()