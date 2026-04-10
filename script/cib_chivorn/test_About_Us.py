import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_privacy_policy(driver):
    wait = WebDriverWait(driver, 30)

    # Open page (already logged in)
    driver.get("https://corporate-uat.apdbank.com.kh")
    driver.maximize_window()

    # --- Click About Us ---
    term_condition_link = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[normalize-space()='About Us']")
        )
    )
    term_condition_link.click()

    time.sleep(10)