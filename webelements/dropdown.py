from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")