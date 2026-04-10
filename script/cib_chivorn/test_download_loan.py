from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_download_loan(driver):
    wait = WebDriverWait(driver, 30)

    # -------------------------------------------------
    # Go directly to the User Settings page (already logged in)
    # -------------------------------------------------
    driver.get("https://corporate-uat.apdbank.com.kh/loans")
    driver.maximize_window()
    time.sleep(3)  # allow page to load

    # -------------------------------------------------
    # Click on Download Statement
    # -------------------------------------------------
    download_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//div[contains(@class,'icon')])[9]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", download_btn)
    driver.execute_script("arguments[0].click();", download_btn)
    time.sleep(0.7)

    # -------------------------------------------------
    # Wait Download Repayment Schedule
    # -------------------------------------------------
    wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//div[contains(@class,'el-overlay-dialog') and .//*[normalize-space()='Download Repayment Schedule']]"
        ))
    )

    time.sleep(0.7)

    # -------------------------------------------------
    # Download PDF
    # -------------------------------------------------
    download = wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//a[contains(@class,'button hsg-button default round') and normalize-space()='Confirm']"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", download)
    driver.execute_script("arguments[0].click();", download)

    time.sleep(0.7)

    # Optional: wait to verify manually
    time.sleep(60)

    # -------------------------------------------------
    # Scroll to top at the end
    # -------------------------------------------------
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(0.5)
