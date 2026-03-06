# login_module_v3.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def do_login(self, username, password, otp="123456"):
        self.driver.get("https://corporate-uat.apdbank.com.kh/login")

        # Enter username
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".el-input:nth-child(3) > .el-input__inner")
        )).send_keys(username)

        # Enter password
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".login-from-item:nth-child(1) .el-form-item__content > .el-input > .el-input__inner")
        )).send_keys(password)

        # Click personal content twice
        self.driver.find_element(By.CSS_SELECTOR, ".personal-content").click()
        self.driver.find_element(By.CSS_SELECTOR, ".personal-content").click()

        # Click login button
        self.driver.find_element(By.ID, "loginBtn").click()

        # OTP
        otp_input = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".otp-items-box .el-input__inner")
            )
        )
        otp_input.send_keys(otp)

        self.driver.find_element(By.CSS_SELECTOR, ".personal-content").click()
        self.driver.find_element(By.ID, "submitForm").click()

        self.driver.execute_script("window.scrollTo(0,0)")
