from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_incoming_other_bank(driver):
    wait = WebDriverWait(driver, 30)

    # -------------------------------------------------
    # Go directly to the User Settings page (already logged in)
    # -------------------------------------------------
    driver.get("https://corporate-uat.apdbank.com.kh")
    driver.maximize_window()
    time.sleep(3)  # allow page to load

    # -------------------------------------------------
    # Click on Notification
    # -------------------------------------------------
    notice_box = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'notice-box en')]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", notice_box)
    driver.execute_script("arguments[0].click();", notice_box)
    time.sleep(1)

    # -------------------------------------------------
    # Expand account box
    # -------------------------------------------------
    notification_box = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//div[contains(@class,'notice-box')])"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", notification_box)

    # 1. Expand if not expanded
    if "expand en" not in notification_box.get_attribute("class"):
        notification_box.click()

    # 2. select Transaction
    transaction_box = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'transactions') and .//*[normalize-space()='Transaction']]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", transaction_box)
    transaction_box.click()
    time.sleep(0.3)

    wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//div[contains(@class,'page-main page-transaction-summary')]"
        ))
    )
    time.sleep(2)

    # Optional: wait to verify manually
    time.sleep(15)

    # -------------------------------------------------
    # Scroll to top at the end
    # -------------------------------------------------
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(0.5)
