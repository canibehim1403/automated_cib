from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_loan_information(driver):
    wait = WebDriverWait(driver, 30)

    # -------------------------------------------------
    # Go directly to the User Settings page (already logged in)
    # -------------------------------------------------
    driver.get("https://corporate-uat.apdbank.com.kh/loans")
    driver.maximize_window()
    time.sleep(3)  # allow page to load

    # -------------------------------------------------
    # Click on Loan Information
    # -------------------------------------------------
    loan_box = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'header') and .//*[normalize-space()='Loan Information']]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", loan_box)
    driver.execute_script("arguments[0].click();", loan_box)
    time.sleep(1)

    # -------------------------------------------------
    # View on Loan Information
    # -------------------------------------------------
    information_box = wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//div[contains(@class,'body expand')]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", information_box)
    driver.execute_script("arguments[0].click();", information_box)
    time.sleep(1)

    # Optional: wait to verify manually
    time.sleep(15)

    # -------------------------------------------------
    # Scroll to top at the end
    # -------------------------------------------------
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(0.5)
