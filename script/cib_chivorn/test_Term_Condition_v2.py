import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_term_condition(driver):
    wait = WebDriverWait(driver, 30)

    # Open page (already logged in)
    driver.get("https://corporate-uat.apdbank.com.kh")
    driver.maximize_window()

    # --- Click Term & Condition link ---
    term_condition_link = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[normalize-space()='Term & Condition']")
        )
    )
    term_condition_link.click()

    # --- Verify dialog is opened ---
    term_condition_title = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'custom-dialog')]//*[normalize-space()='Term & Condition']")
        )
    )

    assert term_condition_title.is_displayed()

    time.sleep(3)
