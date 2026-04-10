from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_payroll_multi(driver):
    wait = WebDriverWait(driver, 30)

    # -------------------------------------------------
    # Go directly to the User Settings page (already logged in)
    # -------------------------------------------------
    driver.get("https://corporate-uat.apdbank.com.kh/payroll")
    driver.maximize_window()
    time.sleep(3)  # allow page to load

    # -------------------------------------------------
    # Choose Single Transfer/ Multiple Transfer
    # -------------------------------------------------
    transfer_type = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'el-tabs__item')][contains(normalize-space(.),'Multi Transfer')]"
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
    # We use 'contains' with normalize-space to be more flexible with hidden formatting
    account_number_locator = (By.XPATH,
                              "//*[contains(@class,'card-box')and .//*[normalize-space()='000 010 657']]")

    # 2. Wait for the elements to appear
    # If it still times out here, the text in the HTML might not match your string exactly
    wait.until(EC.visibility_of_all_elements_located(account_number_locator))

    # 3. Find and Click
    account_cards = driver.find_elements(*account_number_locator)
    if account_cards:
        # Use JS click if standard click fails due to overlays
        driver.execute_script("arguments[0].click();", account_cards[0])
    else:
        print("Account number not found.")

    # -------------------------------------------------
    # To Account
    # -------------------------------------------------
    bank_account = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//div[contains(@class,'el-input')]//input[@maxlength='9'])[5]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", bank_account)
    driver.execute_script("arguments[0].click();", bank_account)
    time.sleep(0.2)
    bank_account.send_keys("000010629")
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
    # Click Add New
    # -------------------------------------------------
    add = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'multi-add-but')][.//span[normalize-space()='Add']]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", add)
    driver.execute_script("arguments[0].click();", add)
    time.sleep(1)

    # -------------------------------------------------
    # To Account No.2
    # -------------------------------------------------
    bank_account = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//input[@placeholder='To Account' and not(@disabled) and not(contains(@style,'display'))])[last()]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", bank_account)
    driver.execute_script("arguments[0].click();", bank_account)
    time.sleep(0.2)
    bank_account.send_keys("000010632")
    time.sleep(0.5)

    # -------------------------------------------------
    # Input Amount
    # -------------------------------------------------
    amount = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//span[normalize-space()='Amount']/ancestor::div[contains(@class,'transfer-input-box')])[last()]//input"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", amount)
    amount.click()
    time.sleep(0.2)
    amount.send_keys("2")
    time.sleep(3)

    # -------------------------------------------------
    # Remark
    # -------------------------------------------------
    remark = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//span[normalize-space()='Remark']/ancestor::div[contains(@class,'el-form-item__content')])[last()]//input"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", remark)
    driver.execute_script("arguments[0].click();", remark)
    time.sleep(0.2)
    remark.send_keys("Cheese Cake Milk Tea")
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
            "//a[contains(@class,'hsg-button') and normalize-space()='Confirm']"
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
    pin_input.send_keys("1111")

    # Optional: wait to verify manually
    time.sleep(15)

    # -------------------------------------------------
    # Scroll to top at the end
    # -------------------------------------------------
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(0.5)
