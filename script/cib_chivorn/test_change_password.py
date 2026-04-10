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
    # Click Change Password
    # -------------------------------------------------
    change_password_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class,'button-box')][.//span[normalize-space()='Change Password']]"
        ))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", change_password_btn)
    driver.execute_script("arguments[0].click();", change_password_btn)

    # -------------------------------------------------
    # Enter Current Password (WITH VALIDATION TRIGGER)
    # -------------------------------------------------
    current_pwd = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//span[normalize-space()='Enter Current Password']"
            "/ancestor::div[contains(@class,'el-form-item__content')]//input"
        ))
    )

    current_pwd.click()
    current_pwd.clear()
    current_pwd.send_keys("Apd@123456789!")

    # Trigger Vue validation
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", current_pwd)
    driver.execute_script("arguments[0].dispatchEvent(new Event('blur'));", current_pwd)

    # -------------------------------------------------
    # Enter New Password (RENDER-SAFE)
    # -------------------------------------------------
    new_pwd_xpath = (
        "//span[normalize-space()='Enter New Password']"
        "/ancestor::div[contains(@class,'el-form-item__content')]//input"
    )

    new_pwd = wait_for_enabled_input(wait, new_pwd_xpath)

    new_pwd.click()
    new_pwd.clear()
    new_pwd.send_keys("Apd@123456789")

    # Trigger Vue validation
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", new_pwd)
    driver.execute_script("arguments[0].dispatchEvent(new Event('blur'));", new_pwd)

    # -------------------------------------------------
    # Re-Enter Password (RENDER-SAFE)
    # -------------------------------------------------
    verify_pwd_xpath = (
        "//span[normalize-space()='Re-Enter Password']"
        "/ancestor::div[contains(@class,'el-form-item__content')]//input"
    )

    verify_pwd = wait_for_enabled_input(wait, verify_pwd_xpath)

    verify_pwd.click()
    verify_pwd.clear()
    verify_pwd.send_keys("Apd@123456789")

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
