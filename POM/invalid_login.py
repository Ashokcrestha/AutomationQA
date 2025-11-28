from selenium import webdriver
from loginpage import LoginPage

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

login_page = LoginPage(driver)
login_page.login("wrong_user", "wrong_pass")

#wait and get error message
error_text = login_page.get_error_message()
print("Error message:", error_text)

driver.quit()