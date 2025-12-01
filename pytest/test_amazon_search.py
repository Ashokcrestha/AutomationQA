#test_amazon_search.py

# run- python -m pytest --alluredir=allure-results--allure serve allure-results

from selenium.webdriver.common.by import By
import time
import allure

@allure.title("Verify Amazon search functionality")
@allure.description("This test checks if searching for 'laptop' shows results correctly on Amazon.")
def test_amazon_search(browser):

    with allure.step("Open Amazon website"):
        browser.get("https://www.amazon.com")
        time.sleep(5)

    with allure.step("Enter search term 'laptop'"):
        search_box = browser.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys("laptop")

    with allure.step("Click on search button"):
        search_button = browser.find_element(By.ID, "nav-search-submit-button")
        search_button.click()

    with allure.step("Wait for results to load"):
        time.sleep(3)

    with allure.step("Verify the results page contains 'laptop'"):
        assert "laptop" in browser.page_source.lower()


@allure.title("Verify Amazon homepage title")
@allure.description("This test checks if the Amazon homepage title contains the word 'Amazon'.")
def test_amazon_title(browser):

    with allure.step("Open Amazon homepage"):
        browser.get("https://www.amazon.com")

    with allure.step("Check page title"):
        assert "Amazon" in browser.title
