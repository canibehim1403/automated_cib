from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_add_template(driver):
    wait = WebDriverWait(driver, 30)

    # -------------------------------------------------
    # Go directly to the User Settings page (already logged in)
    # -------------------------------------------------
    driver.get("https://corporate-uat.apdbank.com.kh/templates")
    driver.maximize_window()
    time.sleep(3)  # allow page to load

    # -------------------------------------------------
    # Click ADD TEMPLATE
    # -------------------------------------------------
    add_template = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'add-template')][.//span[normalize-space()=\"+\"]]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", add_template)
    driver.execute_script("arguments[0].click();", add_template)
    time.sleep(1)

    # -------------------------------------------------
    # Select Service Type
    # -------------------------------------------------
    service_type = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'select-item')][.//span[normalize-space()='Other Account Transfer']]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", service_type)
    driver.execute_script("arguments[0].click();", service_type)
    time.sleep(1)

    # -------------------------------------------------
    # Click Confirm Button
    # -------------------------------------------------
    confirm_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//a[contains(@class,'button hsg-button small round') and normalize-space()='Confirm']"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", confirm_btn)
    driver.execute_script("arguments[0].click();", confirm_btn)
    time.sleep(1)

    # -------------------------------------------------
    # Input Template Name
    # -------------------------------------------------
    input_template_name = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'el-dialog')]//input[@maxlength='30']"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", input_template_name)
    driver.execute_script("arguments[0].click();", input_template_name)
    input_template_name.send_keys("Heekcaa")
    time.sleep(1)

    # -------------------------------------------------
    # Click Confirm Button
    # -------------------------------------------------
    confirm_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//a[contains(@class,'button hsg-button small round') and normalize-space()='Confirm']"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", confirm_btn)
    driver.execute_script("arguments[0].click();", confirm_btn)
    time.sleep(3)

    # -------------------------------------------------
    # Choose Single Transfer/ Multiple Transfer
    # -------------------------------------------------
    transfer_type = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'el-tabs__item')][contains(normalize-space(.),'Single Transfer')]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", transfer_type)
    driver.execute_script("arguments[0].click();", transfer_type)
    time.sleep(1)

    # -------------------------------------------------
    # Expand account box
    # -------------------------------------------------
    account_box = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//div[contains(@class,'account-box-header')])[1]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", account_box)

    # 1. Expand if not expanded
    if "is-active-account-box-header" not in account_box.get_attribute("class"):
        account_box.click()

    # 2. Wait for dropdown content
    wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//div[contains(@class,'account-box')]//div[contains(@class,'card')]"
        ))
    )
    time.sleep(2)

    # 3. select account by number
    account_number = "000 010 656"

    card_box = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            f"//div[contains(@class,'card-box')"
            f" and .//span[normalize-space()='{account_number}']]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", card_box)
    driver.execute_script("arguments[0].click();", card_box)
    time.sleep(0.3)

    # -------------------------------------------------
    # To Account
    # -------------------------------------------------
    to_account = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//div[contains(@class,'custom-input')]//input[@maxlength='9'])[4]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", to_account)
    driver.execute_script("arguments[0].click();", to_account)
    time.sleep(0.2)
    to_account.send_keys("000010632")
    time.sleep(0.5)

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
    remark.send_keys("Guava Passion Green Tea")
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
