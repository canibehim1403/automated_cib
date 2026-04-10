from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_bakong(driver):
    wait = WebDriverWait(driver, 30)

    # -------------------------------------------------
    # Go directly to the User Settings page (already logged in)
    # -------------------------------------------------
    driver.get("https://corporate-uat.apdbank.com.kh/transfer/bakongWallet")
    driver.maximize_window()
    time.sleep(3)  # allow page to load

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
    if "isActive-account-box-header" not in account_box.get_attribute("class"):
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
    account_number = "000 010 657"

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
    wallet_account = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//div[contains(@class,'el-input')]//input[@maxlength='11'])[2]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", wallet_account)
    driver.execute_script("arguments[0].click();", wallet_account)
    time.sleep(0.2)
    wallet_account.send_keys("0969364202")
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
    # Click Transfer button
    # -------------------------------------------------
    transfer_btn = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Transfer")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", transfer_btn)
    transfer_btn.click()
    time.sleep(0.5)

    # -------------------------------------------------
    # Click Confirm Button
    # -------------------------------------------------
    confirm_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//a[contains(@class,'hsg-button') and normalize-space()='Confirm'])[2]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", confirm_btn)
    driver.execute_script("arguments[0].click();", confirm_btn)
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
