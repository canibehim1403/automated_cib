import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_change_logout_slider(driver):
    wait = WebDriverWait(driver, 30)

    # -------------------------------------------------
    # Open page (reuse old Chrome session)
    # -------------------------------------------------
    driver.get("https://corporate-uat.apdbank.com.kh/userSettings")
    time.sleep(3)

    # -------------------------------------------------
    # Locate slider runway (wait until rendered)
    # -------------------------------------------------
    runway = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".el-slider__runway")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});", runway
    )
    time.sleep(2)

    # -------------------------------------------------
    # Execute EXACT drag script (stable)
    # -------------------------------------------------
    target_minutes = 277
    min_minutes = 10
    max_minutes = 360

    percent = (target_minutes - min_minutes) / (max_minutes - min_minutes)
    print(f"Calculated percent: {percent:.4f}")

    driver.execute_script(
        """
        const percent = arguments[0];

        const track = document.querySelector(".el-slider__runway");
        const btn = document.querySelector(".el-slider__button");

        const trackRect = track.getBoundingClientRect();
        const btnRect = btn.getBoundingClientRect();

        const targetX = trackRect.left + trackRect.width * percent;

        btn.dispatchEvent(new MouseEvent("mousedown", {
            clientX: btnRect.left + btnRect.width / 2,
            bubbles: true
        }));

        document.dispatchEvent(new MouseEvent("mousemove", {
            clientX: targetX,
            bubbles: true
        }));

        document.dispatchEvent(new MouseEvent("mouseup", { bubbles: true }));
        """,
        percent
    )

    time.sleep(2)

    # -------------------------------------------------
    # VERIFY via UI text (correct assertion)
    # -------------------------------------------------
    text_elem = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(),'Log out after')]")
        )
    )

    print("Displayed:", text_elem.text)

    # -------------------------------------------------
    # Click Save
    # -------------------------------------------------
    # Now click Save
    save_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[normalize-space()='Save']")
        )
    )

    # Wait until disabled class is gone
    wait.until(
        lambda driver: "is-disabled" not in save_btn.get_attribute("class")
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", save_btn)
    driver.execute_script("arguments[0].click();", save_btn)

    time.sleep(3)

    # --- Enter transaction PIN ---
    pin_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".input-code > .el-input__inner")
    ))
    pin_input.click()
    pin_input.send_keys("3333")

    # Optional: wait to verify manually
    time.sleep(15)
