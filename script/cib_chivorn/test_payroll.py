# test_payroll_v3.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v141.log import clear
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_payroll_flow_v3(driver):
    wait = WebDriverWait(driver, 30)

    # Already logged in → go directly to home
    driver.get("https://corporate-uat.apdbank.com.kh/")
    driver.maximize_window()
    time.sleep(1)  # small wait for page to load

    # Click Payroll menu
    payroll_menu = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".el-menu-item:nth-child(4) img")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", payroll_menu)
    payroll_menu.click()
    time.sleep(0.5)

    # Enter "to account"
    to_account_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".to-account-box .unselected-search:nth-child(2) .el-input__inner")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", to_account_input)
    to_account_input.click()
    time.sleep(0.3)
    to_account_input.send_keys("000010645")
    time.sleep(0.5)

    # Click payroll-single to reveal fields
    payroll_single = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".payroll-single")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", payroll_single)
    payroll_single.click()
    time.sleep(0.5)

    # Amount input
    amount_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".el-form-item:nth-child(1) .transfer-input-box .el-input__inner")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", amount_input)
    amount_input.click()
    time.sleep(0.2)
    amount_input.send_keys("2")
    time.sleep(0.5)

    # # Click payroll-single again if needed
    # payroll_single.click()
    # time.sleep(0.3)

    # Remark input
    remark_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", remark_input)
    remark_input.click()
    time.sleep(0.2)
    remark_input.send_keys("OT_Sunday")
    time.sleep(0.5)

    # Click payroll-single again if needed
    payroll_single.click()
    clear()
    time.sleep(0.3)

    # Click Transfer button
    transfer_btn = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Transfer")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", transfer_btn)
    transfer_btn.click()
    time.sleep(0.5)

    # Click Confirm button
    confirm_btn = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Confirm")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_btn)
    confirm_btn.click()
    time.sleep(0.5)

    # Enter transaction PIN
    pin_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".input-code > .el-input__inner")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pin_input)
    pin_input.click()
    time.sleep(0.2)
    pin_input.send_keys("1111")
    time.sleep(20)

    # Scroll to top at the end
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(0.5)

    print("Payroll v3 transfer completed successfully")
