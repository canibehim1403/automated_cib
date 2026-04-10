from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time


def wait_for_enabled_input(wait, xpath):
    """
    Retry-safe wait for Vue / Element-UI input that becomes enabled
    """

    def _predicate(driver):
        try:
            el = driver.find_element(By.XPATH, xpath)
            return el if el.is_enabled() else False
        except (StaleElementReferenceException, NoSuchElementException):
            return False

    return wait.until(_predicate)


def test_change_password(driver):
    wait = WebDriverWait(driver, 40)

    # -------------------------------------------------
    # Open page
    # -------------------------------------------------
    driver.get("https://corporate-uat.apdbank.com.kh/userSettings")
    driver.maximize_window()

    # -------------------------------------------------
    # Click Change PIN
    # -------------------------------------------------
    change_pin_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'button-box')][.//span[normalize-space()='Change PIN']]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", change_pin_btn)
    driver.execute_script("arguments[0].click();", change_pin_btn)

    # -------------------------------------------------
    # Click Forgot PIN?
    # -------------------------------------------------
    forgot_pin_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//span[normalize-space()='Forgot PIN?']"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", forgot_pin_btn)
    driver.execute_script("arguments[0].click();", forgot_pin_btn)

    # -------------------------------------------------
    # Enter Enter Login Password (WITH VALIDATION TRIGGER)
    # -------------------------------------------------
    login_pwd = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//span[normalize-space()='Enter Login Password']"
            "/ancestor::div[contains(@class,'el-form-item__content')]//input"
        ))
    )

    login_pwd.click()
    login_pwd.clear()
    login_pwd.send_keys("Apd@123456789!")
    time.sleep(3)

    # Trigger Vue validation
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", login_pwd)
    driver.execute_script("arguments[0].dispatchEvent(new Event('blur'));", login_pwd)

    # -------------------------------------------------
    # Enter New PIN (RENDER-SAFE)
    # -------------------------------------------------
    new_pin_xpath = (
        "//span[normalize-space()='Enter New PIN (4 Digits)']"
        "/ancestor::div[contains(@class,'el-form-item__content')]//input"
    )

    new_pin = wait_for_enabled_input(wait, new_pin_xpath)

    new_pin.click()
    new_pin.clear()
    new_pin.send_keys("7373")
    time.sleep(3)

    # Trigger Vue validation
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", new_pin)
    driver.execute_script("arguments[0].dispatchEvent(new Event('blur'));", new_pin)

    # -------------------------------------------------
    # Re-Enter PIN (RENDER-SAFE)
    # -------------------------------------------------
    verify_pin_xpath = (
        "//span[normalize-space()='Re-Enter New PIN (4 Digits)']"
        "/ancestor::div[contains(@class,'el-form-item__content')]//input"
    )

    verify_pin = wait_for_enabled_input(wait, verify_pin_xpath)

    verify_pin.click()
    verify_pin.clear()
    verify_pin.send_keys("7373")
    time.sleep(3)

    # -------------------------------------------------
    # Click Confirm (STATE-BASED WAIT)
    # -------------------------------------------------
    def confirm_enabled(driver):
        try:
            btn = driver.find_element(
                By.XPATH, "//a[contains(@class,'hsg-button') and normalize-space()='Confirm']"
            )
            return btn if "is-disabled" not in btn.get_attribute("class") else False
        except:
            return False

    confirm_btn = wait.until(confirm_enabled)
    driver.execute_script("arguments[0].click();", confirm_btn)
    time.sleep(3)

    # -------------------------------------------------
    # Transaction OTP
    # -------------------------------------------------
    otp_input = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'el-dialog')]//input[@maxlength='6']"
        ))
    )
    otp_input.click()
    otp_input.send_keys("123456")

    # Optional: wait to verify manually
    time.sleep(15)
