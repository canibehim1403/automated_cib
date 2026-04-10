import time

from login_module_v3 import Login


def test_login_flow(driver):
    login = Login(driver)

    login.do_login(
        username="8888100703",
        password="Apd@12345",
        otp="123456"
    )

    print("Login successful! Ready for next flow...")
    time.sleep(10)
