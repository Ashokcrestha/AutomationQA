from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.data_reader import read_csv
import time

def test_login_add_to_cart_logout():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    login_page = LoginPage(driver)
    data = read_csv("data/login_data.csv")

    for row in data:
        print("\n==============================")
        print("Testing user:", row["username"])

        try:
            login_page.open_page()
            login_page.login(row["username"], row["password"])
            time.sleep(2)

            # ---------- SUCCESS LOGIN ----------
            if row["expected"] == "success":
                if "inventory.html" not in driver.current_url:
                    raise Exception("Inventory page NOT opened")

                print("Login successful → Inventory page opened")

                # Add item to cart
                driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

                # Wait for cart badge
                badge = wait.until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
                )

                if badge.text != "1":
                    raise Exception("Cart count incorrect")

                print("PASS: Item added to cart")

                # Open cart page
                driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
                time.sleep(2)

                if "cart.html" not in driver.current_url:
                    raise Exception("Cart page NOT opened")

                cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
                if len(cart_items) == 0:
                    raise Exception("Cart opened but no items found")

                print("PASS: Cart page opened and item verified")

                # Logout
                driver.find_element(By.ID, "react-burger-menu-btn").click()
                time.sleep(1)
                driver.find_element(By.ID, "logout_sidebar_link").click()
                time.sleep(2)

                print("User logged out successfully")

            # ---------- FAILED LOGIN ----------
            else:
                error = login_page.get_error()
                if error == "":
                    raise Exception("Login failed but no error message shown")

                print("Login failed as expected")
                print("Error message:", error)

        except Exception as e:
            print(" TEST FAILED FOR USER:", row["username"])
            print("REASON:", e)

    driver.quit()
