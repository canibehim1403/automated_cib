# test_iR_transfer.py Enhanced Select Account Transfer
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_and_type(driver, locator, text, timeout=30):
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()
    element.clear()
    element.send_keys(text)


def test_iR_transfer(driver):
    wait = WebDriverWait(driver, 30)

    # Go directly to the International Transfer page (already logged in)
    driver.get("https://corporate-uat.apdbank.com.kh/transfer/internationalTransfer")
    driver.maximize_window()
    time.sleep(3)  # allow page to load

    # Close any popup/dialog
    try:
        close_popup = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".el-dialog__close > svg")
        ))
        close_popup.click()
        time.sleep(0.3)
    except:
        pass  # skip if no popup

    time.sleep(3)

    # --- Step 1: expand account box ---
    account_box = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'account-box')]"
        ))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", account_box)
    account_box.click()
    time.sleep(1)

    # --- Step 2: wait for content ---
    wait.until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR,
            ".account-box-content"
        ))
    )
    time.sleep(1)

    # --- Step 3: select account by number ---
    account_number = "000 010 657"

    card_box = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            f"//div[contains(@class,'card-box')"
            f" and .//span[normalize-space()='{account_number}']]"
        ))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card_box)
    card_box.click()
    time.sleep(2)

    # --- Fill recipient info ---
    first_name = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".el-row:nth-child(1) > .el-col:nth-child(1) .el-input__inner")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_name)
    first_name.click()
    first_name.send_keys("John Wich")
    time.sleep(0.3)

    account_number = driver.find_element(
        By.CSS_SELECTOR, ".el-row:nth-child(1) > .el-col:nth-child(2) .el-input__inner"
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", account_number)
    account_number.click()
    account_number.send_keys("000010677")
    time.sleep(1)

    # --- Swift code selection ---
    swift_code_locator = (
        By.XPATH,
        "//span[normalize-space()='Receiver Bank swift Code/BIC']/preceding::input[1]"
    )

    swift_code_el = wait.until(EC.element_to_be_clickable(swift_code_locator))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", swift_code_el)
    swift_code_el.click()
    time.sleep(1)

    swift_option = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'selector-swiftCode-item') and .//span[normalize-space()='LMECGB2L']]"
        ))
    )
    swift_option.click()
    time.sleep(2)

    # --- Small improvement - more stable XPath (If the page layout changes later, this version is safer) ---
    # swift_code_input = (
    #    By.XPATH,
    #    "//span[normalize-space()='Receiver Bank swift Code/BIC']/ancestor::div[contains(@class,'transfer-input-box')]//input"
    # )

    # --- Enter amount ---
    amount_input = driver.find_element(
        By.CSS_SELECTOR, ".transfer-input-currency > .transfer-input-box .el-input__inner"
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", amount_input)
    amount_input.click()
    amount_input.send_keys("2")
    time.sleep(2)

    # --- Currency dropdown selection ---
    # 1. Click the input field itself to open the list
    currency_dropdown = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".transfer-input-currency .el-select .el-input__inner")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", currency_dropdown)
    currency_dropdown.click()
    time.sleep(1)  # Wait for animation

    # 2. Click the specific currency (USD) from the dropdown list
    # This uses the text "USD" which is much safer than relying on CSS hover classes
    usd_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//li[contains(@class, 'el-select-dropdown__item')]//span[text()='USD']")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", usd_option)
    usd_option.click()
    time.sleep(2)

    # --- Recipient address/email/remark ---
    address_input = driver.find_element(
        By.CSS_SELECTOR, ".el-row:nth-child(3) > .el-col > .el-form-item:nth-child(1) .el-input__inner"
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", address_input)
    address_input.click()
    address_input.send_keys("Tokyo Japan")
    time.sleep(0.3)

    email_input = driver.find_element(
        By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner"
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", email_input)
    email_input.click()
    email_input.send_keys("Johnwich@naja.com")
    time.sleep(0.3)

    remark_input = driver.find_element(
        By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner"
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", remark_input)
    remark_input.click()
    remark_input.send_keys("ticket")
    time.sleep(2)

    # --- Select transfer options ---
    transfer_option_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".down-select-button")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", transfer_option_btn)
    time.sleep(3)
    transfer_option_btn.click()

    # --- Select transfer option: OUR ---
    our_option = wait.until(EC.element_to_be_clickable(
        (
            By.XPATH,
            "//div[contains(@class,'select-item')][.//span[contains(text(),'SHA:')]]"
        )
    ))

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        our_option
    )
    time.sleep(0.3)
    our_option.click()

    # --- Confirm transfer ---
    confirm_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Confirm")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_btn)
    time.sleep(3)  # allow footer animation
    confirm_btn.click()

    # Accept terms checkbox
    driver.find_element(By.CSS_SELECTOR, ".el-checkbox__inner").click()
    time.sleep(3)

    # Click Transfer button
    driver.find_element(By.LINK_TEXT, "Transfer").click()
    time.sleep(3)

    # Click final Confirm button
    driver.find_element(By.CSS_SELECTOR, ".page-main > .footer .filled").click()
    time.sleep(3)

    # --- Enter transaction PIN ---
    pin_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".input-code > .el-input__inner")
    ))
    pin_input.click()
    pin_input.send_keys("3333")

    # Optional: wait to verify manually
    time.sleep(15)

    driver.execute_script("window.scrollTo(0,0)")
    print("International Transfer completed successfully")
