import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()

    # ✅ Reuse old Chrome session
    chrome_options.add_argument(
        r"--user-data-dir=C:\Users\UserStandAlone\PycharmProjects\selenium_profile\cib_user"
    )
    chrome_options.add_argument("--profile-directory=Default")

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1050, 652)

    yield driver
    # do NOT quit, leave browser open for persistent login
