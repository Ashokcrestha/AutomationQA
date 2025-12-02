from selenium import webdriver 
from selenium.webdriver.common.by import By
import csv, time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")