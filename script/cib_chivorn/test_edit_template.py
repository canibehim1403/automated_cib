from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_repeat_trx_template(driver):
    wait = WebDriverWait(driver, 30)

    # -------------------------------------------------
    # Go directly to the User Settings page (already logged in)
    # -------------------------------------------------
    driver.get("https://corporate-uat.apdbank.com.kh/templates")
    driver.maximize_window()
    time.sleep(3)  # allow page to load

    # -------------------------------------------------
    # Edit Any TEMPLATE
    # -------------------------------------------------
    edit_template = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'list-item')][.//span[normalize-space()='Heekcaa']]//div[contains(@class,'item-action')]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", edit_template)
    if "active" not in edit_template.get_attribute("class"):
        edit_template.click()
    time.sleep(1)

    # -------------------------------------------------
    # Select Edit
    # -------------------------------------------------
    service_type = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//div[contains(@class,'action-list active')]//div[contains(@class,'icon-more-button')])[2]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", service_type)
    driver.execute_script("arguments[0].click();", service_type)
    time.sleep(3)

    # 2. Wait for Edit Template display
    wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//div[contains(@class,'edit-form')]//input[contains(@class,'el-input__inner')]"
        ))
    )
    time.sleep(0.7)

    # -------------------------------------------------
    # Edit Template Name
    # -------------------------------------------------
    input_template_name = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'el-dialog')]//input[@maxlength='30']"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", input_template_name)
    driver.execute_script("arguments[0].click();", input_template_name)
    input_template_name.clear()
    input_template_name.send_keys("Heekcaa_Cambodia")
    time.sleep(1)

    # -------------------------------------------------
    # Click Confirm Button
    # -------------------------------------------------
    confirm_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//a[contains(@class,'button hsg-button default round') and normalize-space()='Confirm']"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", confirm_btn)
    driver.execute_script("arguments[0].click();", confirm_btn)
    time.sleep(3)

    # -------------------------------------------------
    # Input Amount
    # -------------------------------------------------
    elements = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".transfer-input > .transfer-input-box .el-input__inner")
        )
    )

    amount = elements[6]  # 👈 7th input

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});", amount
    )
    amount.click()
    time.sleep(0.2)
    amount.clear()
    time.sleep(0.2)
    amount.send_keys("3")
    time.sleep(3)

    # -------------------------------------------------
    # Remark
    # -------------------------------------------------
    remark = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//span[normalize-space()='Remark']/ancestor::div[contains(@class,'el-form-item__content')]//input"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", remark)
    driver.execute_script("arguments[0].click();", remark)
    time.sleep(0.2)
    remark.send_keys("Honey Passion Green Tea")
    time.sleep(0.5)

    # -------------------------------------------------
    # Now click Save
    # -------------------------------------------------
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
