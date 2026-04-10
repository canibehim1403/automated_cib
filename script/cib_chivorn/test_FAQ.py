import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_faq(driver):
    wait = WebDriverWait(driver, 30)

    # Open page (already logged in)
    driver.get("https://corporate-uat.apdbank.com.kh")
    driver.maximize_window()
    time.sleep(3)  # allow page to load

    # --- Click FAQ button ---
    click_FAQ = wait.until(EC.element_to_be_clickable(
        (
            By.XPATH,
            "//a[contains(@class,'hsg-button') and normalize-space()='FAQ']"
        )
    ))
    click_FAQ.click()
    time.sleep(2)

    # --- Click FAQ item ---
    faq_item = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//div[@class='collapse-title' and normalize-space()='testing 42']")
    ))

    # Scroll to element (important for Vue UI)
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        faq_item
    )

    # Click (JS click is safer for accordion)
    driver.execute_script("arguments[0].click();", faq_item)

    time.sleep(5)
