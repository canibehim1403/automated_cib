from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_delete_template(driver):
    wait = WebDriverWait(driver, 30)

    # -------------------------------------------------
    # Go directly to the User Settings page (already logged in)
    # -------------------------------------------------
    driver.get("https://corporate-uat.apdbank.com.kh/templates")
    driver.maximize_window()
    time.sleep(3)  # allow page to load

    # -------------------------------------------------
    # DELETE ANY TEMPLATE
    # -------------------------------------------------
    edit_template = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'list-item')][.//span[normalize-space()='DAV']]//div[contains(@class,'item-action')]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", edit_template)
    if "active" not in edit_template.get_attribute("class"):
        edit_template.click()
    time.sleep(1)

    # -------------------------------------------------
    # Select DELETE TEMPLATE
    # -------------------------------------------------
    service_type = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//div[contains(@class,'action-list active')]//div[contains(@class,'icon-more-button')])[3]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", service_type)
    driver.execute_script("arguments[0].click();", service_type)
    time.sleep(3)

    # -------------------------------------------------
    # Wait for Delete Template Display
    # -------------------------------------------------
    wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//div[contains(@class,'el-dialog__footer')]//a[contains(@class,'button hsg-button default round')]"
        ))
    )
    time.sleep(0.7)

    # -------------------------------------------------
    # Click Cancel/Confirm Button
    # -------------------------------------------------
    confirm_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//a[contains(@class,'button hsg-button default round') and normalize-space()='Confirm']"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", confirm_btn)
    driver.execute_script("arguments[0].click();", confirm_btn)
    time.sleep(0.7)

    # -------------------------------------------------
    # Wait for PIN Box Display
    # -------------------------------------------------
    wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//div[contains(@class,'custom-dialog')]//div[contains(@class,'el-dialog') and normalize-space()='Enter PIN']"
        ))
    )
    time.sleep(0.7)

    # -------------------------------------------------
    # --- Enter transaction PIN ---
    # -------------------------------------------------
    pin_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".input-code > .el-input__inner")
    ))
    pin_input.click()
    pin_input.send_keys("7373")

    # Optional: wait to verify manually
    time.sleep(15)

    # -------------------------------------------------
    # Scroll to top at the end
    # -------------------------------------------------
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(0.5)

    print("Edit Template completed successfully")
