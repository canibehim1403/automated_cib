import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()

    # ✅ Reuse old Chrome session
    chrome_options.add_argument(
        r"--user-data-dir=D:\selenium_profile\cib_user"
    )
    chrome_options.add_argument("--profile-directory=Default")

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1296, 688)

    yield driver
