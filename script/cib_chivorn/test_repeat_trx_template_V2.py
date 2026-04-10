# Not Yet Fix  //https://chatgpt.com/share/6969a2bd-f6e0-8003-bfbc-381c181d2cac
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
    # Choose Any TEMPLATE
    # -------------------------------------------------
    repeat_trx = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'list-item')][.//span[normalize-space()='Cafe Shopper']]//div[contains(@class,'item-action')]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", repeat_trx)
    if "active" not in repeat_trx.get_attribute("class"):
        repeat_trx.click()
    time.sleep(1)

    # -------------------------------------------------
    # Select Repeat TRX
    # -------------------------------------------------
    service_type = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "(//div[contains(@class,'action-list active')]//div[contains(@class,'icon-more-button')])[1]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", service_type)
    driver.execute_script("arguments[0].click();", service_type)
    time.sleep(3)

    # 2. Wait for dropdown content
    wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            "(//div[contains(@class,'transfer-input-box')]//input[contains(@class,'el-input__inner')])[7]"
        ))
    )
    time.sleep(2)

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
    time.sleep(3)

    # -------------------------------------------------
    # Click Confirm button
    # -------------------------------------------------
    confirm_btn = wait.until(
        EC.presence_of_element_located((
            By.XPATH,
            "//div[contains(@class,'footer-button-box')]//a[contains(@class,'button') and contains(@class,'hsg-button') and normalize-space()='Confirm']"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", confirm_btn)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", confirm_btn)

    time.sleep(3)
    # -------------------------------------------------
    # Enter transaction PIN
    # -------------------------------------------------
    pin_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".input-code > .el-input__inner")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pin_input)
    pin_input.click()
    time.sleep(0.2)
    pin_input.send_keys("7373")
    time.sleep(20)

    # -------------------------------------------------
    # Scroll to top at the end
    # -------------------------------------------------
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(0.5)

    print("Payroll v3 transfer completed successfully")
