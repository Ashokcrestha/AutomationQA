import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    print("\nOpening Chrome browser...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print("\nClosing browser...")
    driver.quit()
