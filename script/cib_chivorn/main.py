from selenium import webdriver
from test_payroll import test_payroll_flow_v3
from test_iR_transfer_V9 import test_iR_transfer
import time

def main():
    # 1. Initialize WebDriver (Chrome in this example)
    driver = webdriver.Chrome()  # make sure chromedriver is in PATH
    driver.maximize_window()

    try:
        # 2. Run Payroll script first
        print("Starting Payroll transfer...")
        test_payroll_flow_v3(driver)
        print("Payroll transfer done.\n")

        time.sleep(2)  # small wait between scripts

        # 3. Run International Transfer script next
        print("Starting International Transfer...")
        test_iR_transfer(driver)
        print("International Transfer done.\n")

    finally:
        # 4. Close browser at the end
        driver.quit()

if __name__ == "__main__":
    main()
