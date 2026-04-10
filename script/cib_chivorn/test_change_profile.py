from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_change_profile(driver):
    wait = WebDriverWait(driver, 30)
    driver.get("https://corporate-uat.apdbank.com.kh/userSettings")
    driver.maximize_window()

    # Find the hidden <input type="file"> directly
    file_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )

    file_path = r"C:\Users\UserStandAlone\Downloads\Telegram Desktop\photo_3_2026-01-10_05-59-16.jpg"
    driver.execute_script("arguments[0].style.display = 'block';", file_input)
    file_input.send_keys(file_path)

    time.sleep(10)

    # Now click Save
    save_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class,'hsg-button') and normalize-space()='Save']"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_btn)
    save_btn.click()
    time.sleep(3)

    # --- Enter transaction PIN ---
    pin_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".input-code > .el-input__inner")
    ))
    pin_input.click()
    pin_input.send_keys("3333")

    # Optional: wait to verify manually
    time.sleep(15)
