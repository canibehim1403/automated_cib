from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_change_department(driver):
    wait = WebDriverWait(driver, 30)

    # Go directly to the User Settings page (already logged in)
    driver.get("https://corporate-uat.apdbank.com.kh/userSettings")
    driver.maximize_window()
    time.sleep(3)  # allow page to load

    # Locate department input by label
    department_input = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[normalize-space()='Department']/following::input[1]")
        )
    )

    # Click, clear old department, input new department
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", department_input)
    department_input.click()
    department_input.clear()
    department_input.send_keys("Digital Banking")
    time.sleep(3)

    # Now click Save
    save_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[normalize-space()='Save']")
        )
    )

    # Wait until disabled class is gone
    wait.until(
        lambda driver: "is-disabled" not in save_btn.get_attribute("class")
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", save_btn)
    driver.execute_script("arguments[0].click();", save_btn)

    time.sleep(3)

    # --- Enter transaction PIN ---
    pin_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".input-code > .el-input__inner")
    ))
    pin_input.click()
    pin_input.send_keys("3333")

    # Optional: wait to verify manually
    time.sleep(15)
