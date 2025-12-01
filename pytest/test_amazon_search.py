#test_amazon_search

from selenium.webdriver.common.by import By
import time
import allure

allure.title("Verify Amazon search functionality")
allure.description("This test checks if searching for 'laptop' shows  results correctly on Amazon.")
def test_amazon_search(browser):
 with allure.step("Open Amazon website"):
  browser.get("https://www.amazon.com")
  time.sleep(4)

with allure.step("Enter search term 'laptop'"):
   search_box = browser.find_element(By.ID, "twotabsearchtextbox")
   search_box.send_keys("laptop")

